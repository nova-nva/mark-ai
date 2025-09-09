from crewai import Task, Agent
from ...schemas.hia_ouput import HIAOutput

def build_research_task(agent: Agent) -> Task:
    return Task (
        agent=agent,
        description=(
            "If the model provided by the Human Input Analyst contains `critical_errors` field, do not execute any task. Just return the critical_errors field. "
            "Otherwise Use the model and check if `brand_tone` and `platform` fields are marked with None. "
            "If these are None, fill them with appropiate responses based on well foundated marketing strategies. "
            "If you get to choose platform field, really consider TikTok since lately is really used to attract people. "
            "Do not edit any existing info."
            "For each field you fill on the output, provide a brief explanation of why you chose to do that on strategic_reaseons. "
        ),
        expected_output=(
            "Return the same object schema with the missing parts now complete"
        ),
        output_pydantic=HIAOutput
    )

def build_tendencies_task(agent: Agent) -> Task:
    return Task (
        agent=agent,
        description=(
            "If the model provided by the previous agent contains `critical_errors` field, do not execute any task. Just return the critical_errors field.. "
            
            "Otherwise search about the last tendencies and trends with a week from the current date. "
            "Do not edit any existing info. "
            "Carefully look if any trend aligns with the info provided. "
            "If no `platform` was provided, feel free to suggest also what social media platform would be best to align with the trends and the request. Take into really account Tik Tok, since it shows a facility to spread info among many people. "
            "Return suggestions on what are the current trends right now, what platform should we use, and how our post should align with them. Put all of this info in a sentence inside `trend_info0 field`. "
            "For each field you fill on the output, provide a brief explanation of why you chose to do that as strategic_reasons. "
        ),
        expected_output=(
            "Return the same object schema with trend_info field now complete. "
        ),
        output_pydantic=HIAOutput
    )