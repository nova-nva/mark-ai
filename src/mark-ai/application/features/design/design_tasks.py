from crewai import Task, Agent
from ...schemas.design_schema import DesignConceptModel

def build_design_task(agent: Agent, structured_input: Task, post_content: Task) -> Task:
    return Task (
        agent=agent,
        description=(
            "If the previous models provided any `critical_errors` field, do not execute any task. Just return that field content. "
            "Otherwise, generate 1 CONSISTENT graphic design concept. "
            "You have two provided pieces of info that come from previous tasks: \n"
            "1. HIAOutput: Structured briefing based on the human input. \n"
            "2. Post content: The content that will posted for the user prompt. \n"
            "Generate a Design Concept with this points: Suggested color palette (3-5 hex colors), Suggested typography, Strategic reasons (why is it useful for our objectives and audience). " 
            "You must follow logic structures and the input provided. "
        ),
        context=[structured_input, post_content], 
        expected_output=(
            "Return the Design Concept"
        ),
        output_pydantic=DesignConceptModel
    )