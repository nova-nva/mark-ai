from crewai import Task, Agent
from ....schemas.hia_ouput import HIAOutput

def build_process_input_task(agent: Agent) -> Task:
    """
    Input: {prompt}
    Expected output: 
        - 'Summary:' Extracted points list
        - 'Explanation:' Reasons why the points on summary were chosen list
    """
    return Task (
        agent=agent,
        description=(
            "Analyze provided prompt and structure it on the HIAOutput schema:"
            "If you can not find any of the points, just put null. Do not infere or create data on your own"
            # "Finally, you must provide a brief and concise explanation of why you chose to put each part of the info on each point"
            "Avoid speculation and do not hallucinate"
        ),
        expected_output=(
            "Return ONLY the object schema without extra points"
            # "Explanation: <reasons why you chose to put the info on the points>"
        ),
        output_pydantic=HIAOutput
    )