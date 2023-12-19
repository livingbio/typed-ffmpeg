from typing import Any

import pytest


def filter_response_headers(response: dict[str, Any]) -> dict[str, Any]:
    # Modify or exclude headers as needed
    response["headers"].pop("openai-organization", None)  # Exclude a header from the response
    return response


@pytest.fixture(scope="module")
def vcr_config() -> dict[str, Any]:
    return {
        "filter_headers": ["authorization", "api-key"],  # Be sure to match the case of the header exactly
        "before_record_response": filter_response_headers,
    }
