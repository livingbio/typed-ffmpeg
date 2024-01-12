try:
    # pydantic >= 2.0
    from pydantic import BaseModel, model_validator

    model_validator_after = model_validator(mode="after")
except ImportError:
    # pydantic < 2.0
    from pydantic import BaseModel, root_validator

    model_validator_after = root_validator  # type: ignore


__all__ = ["BaseModel", "model_validator_after"]
