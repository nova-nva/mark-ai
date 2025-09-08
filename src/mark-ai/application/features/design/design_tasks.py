from crewai import Task, Agent
from ...schemas.design_schema import DesignConceptModel

def build_design_task(agent: Agent, structured_input: Task, post_content: Task) -> Task:
    return Task (
        agent=agent,
        description=(
            "If the previous models provided any `critical_errors` field, do not execute any task. Just return that field content. "

            "Otherwise, generate 1 CONSISTENT graphic design concept foundated on the info provided. "
            "You have two provided pieces of info that come from previous tasks: \n"
            "1. HIAOutput: Structured briefing based on the user prompt. \n"
            "2. Post content: The post content generated from the user prompt. \n"

            "Generate a Design Concept that should be posted with the content. " 
            "You should choose based on the message we want to give and must align the concepts provided. "

            "Output field guide: \n" 
            "design_concept: What piece of art should we use (may be an image, an infographic, a carousel, a video, etc. but only 1) along with a concept of that piece of art in a clear, direct and actionable brief to be implemented by a designer. \n"
            "color_palette: what color palette is suggested based on info provided (3-5 HEX colors). \n"
            "typography: proposed typography based on info provided. \n"
            "visual_elements: clear and concise visual elements that should be included on the art. \n"
            "layout: how the elements proposed should be disposed. \n"
            "strategic_reasons: foundations of why you chose to go with each proposal on each filed. you MUST add a explanation of why you chose that specific piece of art. \n"

            "You must follow logic structures and the input provided. "
        ),
        context=[structured_input, post_content], 
        expected_output=(
            "Return the Design Concept"
        ),
        output_pydantic=DesignConceptModel
    )