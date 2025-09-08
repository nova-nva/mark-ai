from crewai import Task, Agent
from ....schemas.hia_ouput import HIAOutput

def build_process_input_task(agent: Agent) -> Task:
    return Task (
        agent=agent,
        description=(
            "Analyze provided prompt and structure it on the HIAOutput schema. "
            "If you can not find any of the points, just put None. Do not infere or create data on your own. "
            "Avoid speculation and do not hallucinate. \n"

            "Field guide: \n"
            "products: what is (or what are) the product(s) to be promoted? what are the details? \n"
            "objectives: why the user wants to promote the product. what are the objectives. \n"
            "post_type: in what scenario we are. some common types are: launch, offer/discount, educational/informative, inspirational/motivational, entertaining. If None of the mentioned above fit on the prompt, you can classify with another appropiate type. \n"
            "brand_tone: what is the tone that the company or user want to use for the post. \n"
            "platform: what is the target social media platform. \n"
            "extra_info: any info that did not match any of the previous points. \n"
            "strategic_reasons: foundations of why you chose to classify each part on each filed. \n"
            
            "At the end of the process, only if the fields `products`, `objectives`, `post_type` are marked with None at the end, add to critical_errors list: `Missing important info` plus a brief explanation of what is missing. "
            "if other fields are missing, do not touch critical_errors and continue the process. "
        ),
        expected_output=(
            "Return ONLY the object schema without extra points"
            # "Explanation: <reasons why you chose to put the info on the points>"
        ),
        output_pydantic=HIAOutput
    )