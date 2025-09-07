from crewai import Crew, LLM
import os
from .agents.input_parser import build_input_parser
from .tasks.process_input import build_process_input_task

# LLM configs
def _gemini_llm():
    # config
    return LLM(
        model="gemini/gemini-1.5-flash",
        api_key = os.getenv("GEMINI API KEY"),
        temperature=0
    )

# Input Crew Processes
def build_input_crew(llm=None) -> Crew:
    parser = build_input_parser(llm=llm)
    t1 = build_process_input_task(parser)
    return Crew(agents=[parser], tasks=[t1])


def run_input_feature(inp: str, llm=_gemini_llm()):
    crew = build_input_crew(llm=llm)
    result_text = crew.kickoff(inputs={"prompt": inp})
    return result_text

