from crewai import Crew, Process, LLM
import os

# features import
from ..features.input.agents.input_parser import build_input_parser
from ..features.input.tasks.process_input import build_process_input_task
from ..features.research.research_agents import build_researcher
from ..features.research.research_tasks import build_research_task
from ..features.research.research_agents import build_tendency_researcher
from ..features.research.research_tasks import build_tendencies_task
from ..features.copywriting.copy_agents import build_copywriter_agent
from ..features.copywriting.copy_tasks import build_copy_task
from ..features.design.design_agents import build_designer_agent
from ..features.design.design_tasks import build_design_task
from ..features.output.output_agents import build_output_agent
from ..features.output.output_tasks import build_output_task


# LLM configs
def _gemini_llm():
    # config
    return LLM(
        model="gemini/gemini-1.5-flash",
        api_key = os.getenv("GEMINI_API_KEY"),
        temperature=0
    )

# flow
def run_flow(user_input: str):

    # agents
    input_parser_agent = build_input_parser(llm=_gemini_llm())
    research_agent = build_researcher(llm=_gemini_llm())
    trends_agent = build_tendency_researcher(llm=_gemini_llm())
    copywriter_agent = build_copywriter_agent(llm=_gemini_llm())
    designer_agent = build_designer_agent(llm=_gemini_llm())
    output_agent = build_output_agent(llm=_gemini_llm())

    #tasks
    input_task = build_process_input_task(input_parser_agent)
    marketing_research_task = build_research_task(research_agent)
    trends_research_task = build_tendencies_task(trends_agent)
    content_task = build_copy_task(copywriter_agent)
    design_task = build_design_task(designer_agent, trends_research_task, content_task)
    output_task = build_output_task(output_agent, [trends_research_task, content_task, design_task])

    crew = Crew(
        agents=[input_parser_agent, research_agent, trends_agent, copywriter_agent, designer_agent, output_agent],
        tasks=[input_task, marketing_research_task, trends_research_task, content_task, design_task, output_task],
        process=Process.sequential,
    )
    
    outputs = crew.kickoff(inputs={"prompt": user_input})
    return outputs
    
