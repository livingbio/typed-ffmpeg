from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv(override=True)

client = AzureOpenAI(azure_deployment="gpt35")
result = client.chat.completions.create(
    messages=[{"role": "user", "content": f"hello world"}],
    model="gpt-3.5-turbo",
)
print(result.choices[0].message.content)
