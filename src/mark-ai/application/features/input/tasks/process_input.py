from crewai import Task, Agent
from ....schemas.hia_ouput import HIAOutput

def build_process_input_task(agent: Agent) -> Task:
    return Task (
        agent=agent,
        description=(
            "Analyze provided prompt and structure it on the HIAOutput schema:"
            "If you can not find any of the points, just put None. Do not infere or create data on your own"
            "Avoid speculation and do not hallucinate. "
            "If at the end of the process, only if the fields `products`, `objectives`, `post_type` are marked with None at the end, add to critical_errors list: `Missing important info`"
            "if other fields are missing, do not touch critical_errors and continue the process "
        ),
        expected_output=(
            "Return ONLY the object schema without extra points"
            # "Explanation: <reasons why you chose to put the info on the points>"
        ),
        output_pydantic=HIAOutput
    )