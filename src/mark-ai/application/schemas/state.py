from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from ..schemas.hia_ouput import HIAOutput

Route = Literal["start", "break", "researcher", "copywriter", "designer", "stop"]

class FlowState(BaseModel):
    # inputs and results
    raw_input: str = Field(..., description="user initial prompt")
    hia: Optional[HIAOutput] = None

    # flow signals
    route: Route = "start"
    errors: List[str] = Field(default_factory=list)

    # helpers
    def missing_core(self) -> List[str]:
        missing = []
        if not (self.hia and self.hia.products):
            missing.append("products")
        if not (self.hia and self.hia.objectives):
            missing.append("objectives")
        if not (self.hia and self.hia.post_type):
            missing.append("post_type")
        return missing
    
    def missing_info(self) -> List[str]:
        missing = []
        if not (self.hia and self.hia.brand_tone):
            missing.append("brand_tone")
        if not (self.hia and self.hia.platform):
            missing.append("platform")
        if not (self.hia and self.hia.extra_info):
            missing.append("extra_info")
        return missing
    
    def is_ready_for_research(self) -> bool:
        return self.hia is not None and not self.missing_core()
    
    def is_ready_for_content(self) -> bool:
        return self.hia is not None and not self.missing_core() and not self.missing_info()
    
    # next steps to tak
    def next_after_hia(self) -> Route:
        # default
        if self.missing_core():
            return "break"
        if self.missing_info():
            return "researcher"
        return "copywriter"