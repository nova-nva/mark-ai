from typing import Optional, List
from pydantic import BaseModel, Field, field_validator

class DesignConceptModel(BaseModel):
    # design concept
    design_concept:     Optional[str] = Field(None, description="main design concept")
    color_palette:      Optional[str] = Field(None, description="color palette to use")
    typography:         Optional[str] = Field(None, description="proposed typography")
    visual_elements:    Optional[str] = Field(None, description="visual elements")
    layout:             Optional[str] = Field(None, description="layout")

    # trazability
    critical_errors:    Optional[List[str]] = Field(None, description="critical issues that prevent us from doing the task")
    strategic_reasons:  Optional[List[str]] = Field(None, description="list of why the agents took each decision")

    # @field_validator("title", "content", "ctas", "hashtags")
    # def empty_to_none(cls, v):
    #     if v is None:
    #         return None
    #     if isinstance(v, str) and v.strip() in {"", "N/A", "not found", "null", "None"}:
    #         return None
    #     return v
