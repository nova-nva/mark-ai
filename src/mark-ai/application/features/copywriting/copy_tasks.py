from crewai import Task, Agent
from ...schemas.post_schema import PostContentModel

def build_copy_task(agent: Agent) -> Task:
    return Task (
        agent=agent,
        description=(
            "If the model provided by the Human Input Analyst contains `critical_errors` field, do not execute any task. Just return that field content. "
            "Otherwise use the model to create creative, gramatically correct and coherent content to post. "
            "You must follow logic structures and the input provided. "
            "For each field you fill on the output, add a new item to strategic_reasons list filed providing a brief explanation of why you chose to do that. "
        ),
        expected_output=(
            "Return all the content that will belong to the Post"
        ),
        output_pydantic=PostContentModel
    )