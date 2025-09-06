from crewai import Task, Agent

def build_process_input_task(agent: Agent) -> Task:
    """
    Input: {prompt}
    Expected output: 
        - 'Summary:' Extracted points list
        - 'Explanation:' Reasons why the points on summary were chosen list
    """
    return Task (
        description=(
            "Analyze provided prompt and extract the following points:"
            "Mandatory points: Products, Objectives, Post Type"
            "Optional points: Brand Tone, Platform, Extra Info"
            "If you can not find any of the points, just put 'Not found' on the results"
            "You can use 'Extra Info' point to fill any information on the prompt that do not match with the other points"
            "Finally, you must provide a brief and concise explanation of why you chose to put each part of the info on each point"
            "Avoid speculation and do not hallucinate"
        ),
        agent=agent,
        expected_output=(
            "Summary: <all the points on the description>"
            "Explanation: <reasons why you chose to put the info on the points>"
        )
    )