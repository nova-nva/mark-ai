from crewai import Task, Agent
from ...schemas.hia_ouput import HIAOutput

def build_copy_task(agent: Agent) -> Task:
    return Task (
        agent=agent,
        description=(
            "If the model provided by the Human Input Analyst contains `critical_errors` field, do not execute any task. Just return that field content. "
            "Otherwise use the model to create creative, gramatically correct and coherent content to post. "
            "You must follow logic structures and the input provided. "
        ),
        expected_output=(
            "Return the content that will belong to the Post"
        ),
    )