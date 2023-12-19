import json
import re
from typing import Any

import pydantic
from dotenv import load_dotenv
from openai import AzureOpenAI

from .parser import FilterDocument

# Load environment variables from .env file
load_dotenv(override=True)


class Filter(pydantic.BaseModel):
    name: str
    source: str
    description: str
    ref: pydantic.HttpUrl
    parameters: list[dict[str, str]] = []
    json_schema: dict[str, Any] = {}


def extract_json_code(body: str) -> str:
    re_json = re.compile(r"```(.*)```", re.DOTALL | re.MULTILINE)

    match = re_json.findall(body)
    if match:
        if match[0].strip().startswith("json"):
            return match[0].strip()[4:]
        return match[0]

    return body


def generate_json_schema(doc: FilterDocument) -> dict[str, dict[str, Any]]:
    client = AzureOpenAI(azure_deployment="gpt35")

    SYSTEM_PROMPT = {
        "role": "system",
        "content": """
- You possess expertise in FFmpeg.
- I kindly request your assistance in the conversion of specific FFmpeg filter document options into a JSON schema.
- Please be aware that certain FFmpeg filter documents may require reference to other documents, which will be provided for your thorough consideration.
- Only generate the JSON schema for the asking filter, and not any other filters.
""",
    }

    output = {}
    for filter_name in doc.filter_names:
        ref_buffer = ""

        if not doc.parameters:
            output[filter_name] = {}
            continue

        for ref in doc.refs:
            if ref.exists():
                ref_buffer += ref.read_text() + "\n"
            else:
                print(f"Missing reference: {ref}")

        USER_PROMPT = {
            "role": "user",
            "content": f"""please generate JSON Schema for {filter_name}'s options only
## {filter_name}
{doc.body}
## reference
{ref_buffer}""",
        }

        result = client.chat.completions.create(
            messages=[SYSTEM_PROMPT, USER_PROMPT],
            model="gpt-3.5-turbo",
            temperature=0.0,
        )
        output[filter_name] = json.loads(extract_json_code(result.choices[0].message.content))

    return output


def parse_schema(info: FilterDocument) -> list[Filter]:
    json_schemas = generate_json_schema(info)

    output = []

    for filter_name in info.filter_names:
        filter_name = filter_name.strip()
        json_schema = json_schemas[filter_name]
        output.append(
            Filter(
                name=filter_name,
                source=info.body,
                description=info.description,
                ref=info.url,
                parameters=info.parameters,
                json_schema=json_schema,
            )
        )

    return output
