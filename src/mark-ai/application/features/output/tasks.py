from crewai import Task, Agent
from typing import List

def build_output_task(agent: Agent, previous_outputs: List[Task]) -> Task:
    return Task (
        agent=agent,
        description=(
            "If the previous models provided any `critical_errors` field, do not execute any task. Just return that field content. "
            "Otherwise, generate a general Crew Output. "
            "You have three provided pieces of info where previous agents provided extra info: \n"
            "1. HIAOutput: Structured briefing based on the human input. \n"
            "2. PostContentModel: The content that will posted for the user prompt. \n"
            "3. DesignConceptModel: A design concept that aligns with the Post and human input. \n"
            "Generate a Human Readable Final Response markdown content with the points on the following order:. " 
            "1. Standarized Targets: HIAOutput (all content) "
            "2. Standarized Targets strategic reasons: HIAOutput.strategic_reasons | Foundations of the proposed procedures "
            "3. Post Content: PostContentModel (all content) "
            "4. Post Content strategic reasons: PostContentModel.strategic_reasons | Foundations of the proposed procedures "
            "5. Design Concept: DesignConceptModel (all content) "
            "6. Design Concept strategic reasons: HIAOutput.strategic_reasons | Foundations of the proposed procedures "
            
            "Provide the responses in a way that a human can understand and apply all the research properly. "
        ),
        context=previous_outputs, 
        expected_output=(
            "Return the Human Readable Final Response"
        ),
    )