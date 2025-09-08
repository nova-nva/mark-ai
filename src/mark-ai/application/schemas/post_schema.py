from typing import Optional, List
from pydantic import BaseModel, Field, field_validator

class PostContentModel(BaseModel):
    # post
    title:     Optional[str] = Field(None, description="post title")
    content:   Optional[str] = Field(None, description="post content")
    ctas:      List[Optional[str]] = Field(None, description="post call to actions")
    hashtags:  List[Optional[str]] = Field(None, description="post hashtags")

    # trazability
    critical_errors: Optional[List[str]] = Field(None, description="critical issues that prevent us from doing the task")
    strategic_reasons: Optional[List[str]] = Field(None, description="list of why the agents took each decision")

    @field_validator("title", "content", "ctas", "hashtags")
    def empty_to_none(cls, v):
        if v is None:
            return None
        if isinstance(v, str) and v.strip() in {"", "N/A", "not found", "null", "None"}:
            return None
        return v
