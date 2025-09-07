from crewai import Agent

def build_copywriter_agent(llm=None) -> Agent:
    return Agent (
        role="Copywriting Expert",
        goal="Create the Post Content considering all inputs provided by the Marketing Research ",
        backstory=(
            "You are creative and a great Copywriting Expert. "
            "You also avoid speculation or hallucination. "
            "Work only on the information provided."
        ),
        llm=llm,
        verbose=True,
    )