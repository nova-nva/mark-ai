from crewai import Task, Agent
from ...schemas.hia_ouput import HIAOutput

def build_research_task(agent: Agent) -> Task:
    """
    Input: {HIAOuptut}
    Expected output: 
        - 'Summary:' the missing points completion with well foundationed info
        - 'Explanation:' Reasons why the points on summary were chosen
    """
    return Task (
        agent=agent,
        description=(
            "If the model provided by the Human Input Analyst contains `critical_errors` field, do not execute any task. Just return the original object. "
            "Otherwise Use the model and check if `brand_tone` and `platform` fields are marked with None. "
            "If these are None, fill them with appropiate responses based on well foundated marketing strategies. "
            "Do not edit any existing info."
            "For each field you fill on the output, provide a brief explanation of why you chose to do that on strategic_reaseons. "
        ),
        expected_output=(
            "Return the same object schema with the missing parts now complete"
        ),
        output_pydantic=HIAOutput
    )