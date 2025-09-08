from crewai import Agent

def build_output_agent(llm=None) -> Agent:
    return Agent (
        role="Agent Ouput Analyst",
        goal="Provide a Human Readable response based on the process of the previous agents",
        backstory=(
            "You are direct, helpful, detail worried. "
            "You avoid speculation or hallucination. "
            "Work only on the information provided."
        ),
        llm=llm,
        verbose=True,
    )