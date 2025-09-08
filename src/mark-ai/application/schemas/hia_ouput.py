from typing import Optional, List
from pydantic import BaseModel, Field, field_validator

class HIAOutput(BaseModel):
    # prompt info
    products:   Optional[str] = Field(None, description="what is the product to be promoted")
    objectives: Optional[str] = Field(None, description="why do the user want to promote the product. what's the target.")
    post_type:  Optional[str] = Field(None, description="in what scenario we are. lauch, discount, educational, etc.")
    brand_tone: Optional[str] = Field(None, description="what is the ideal tone of the company or user that want to use for the post")
    platform:   Optional[str] = Field(None, description="what is the target social media platform")
    extra_info: Optional[str] = Field(None, description="any info that did not match any of the previous points")

    # trazability
    critical_errors: Optional[List[str]] = Field(None, description="critical issues that prevent us from doing the task")
    strategic_reasons: Optional[List[str]] = Field(None, description="List of why the agents took each decision")

    @field_validator("products", "objectives", "post_type", "brand_tone", "platform", "extra_info")
    def empty_to_none(cls, v):
        if v is None:
            return None
        if isinstance(v, str) and v.strip() in {"", "N/A", "not found", "null", "None"}:
            return None
        return v
    
REQUIERED_FIELDS: List[str] = ["products", "objectives", "post_type"]
