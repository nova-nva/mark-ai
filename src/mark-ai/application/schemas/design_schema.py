from typing import Optional, List
from pydantic import BaseModel, Field, field_validator

class DesignConceptModel(BaseModel):
    # design concept
    design_concept:     Optional[str] = Field(None, description="main design concept of what we are going to create with a clear and actionable descripition to be implemented by a designer")
    color_palette:      Optional[str] = Field(None, description="what colors palette is suggested based on info provided. ")
    typography:         Optional[str] = Field(None, description="proposed typography based on info provided")
    visual_elements:    List[Optional[str]] = Field(None, description="clear and concise visual elements that should be included on the art.")
    layout:             Optional[str] = Field(None, description="how the layout should be disposed. ")

    # trazability
    critical_errors:    Optional[List[str]] = Field(None, description="critical issues that prevent us from doing the task")
    strategic_reasons:  Optional[List[str]] = Field(None, description="list of why the agents took each decision")
