from crewai import Task, Agent
from typing import List

def build_output_task(agent: Agent, previous_outputs: List[Task]) -> Task:
    return Task (
        agent=agent,
        description=(
            "If there is a `critical_errors` field in the context, do not execute anything and return exactly that content. "
           
            "Otherwise, create an integrated, human-friendly response based on HIAOutput, PostContentModel, and DesignConceptModel. "
            "Transform and synthesize: do not list raw fields or attribute names; rewrite everything in natural prose. \n"
            "Do not invent data; Use only the info you were provided and make sure of not missing anything. "
            
            "Structure the answer in Markdown with the following sections: \n"
            "## Executive Summary (max 2 lines; Based on HIAOutput); \n"
            "- Post type: \n"
            "- Brand tone: \n"
            "- Target platform: \n"
            "- Current related trends: \n"
            "#### Summary Foundations (Based on HIAOutput.strategic_reasons)"
            "## Post (final copy with CTAs if applicable, based on PostContentModel); \n"
            "#### Post Foundations (Based on PostContentModel.strategic_reasons)"
            "## Suggested Design \n"
            "- Visual format: (besides giving the answer, explain why that format was chosen)\n"
            "- Specific art: \n"
            "- Design Concept: \n"
            "- Visual elements, layout and instructions: \n"
            "- Look & feel, colors, typography, composition: \n"
            "#### Design Foundations (Based on DesignConceptModel.strategic_reasons)"
            
            "Provide the responses in a way that a human can understand and apply all the research properly. "
            "avoid unnecessary technical jargon, and never expose field names. "
        ),
        context=previous_outputs, 
        expected_output=(
            "A polished, human-readable Markdown with the specified sections; "
            "if `critical_errors` exists, return only that content."
        ),
    )