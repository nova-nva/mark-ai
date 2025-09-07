from crewai import Agent

def build_researcher(llm=None) -> Agent:
    return Agent (
        role="Marketing Strategy Researcher",
        goal="Detect the missing points (the ones marked with None) research about the best Brand Tone and Social Media Platform target to launch our marketing campaign",
        backstory=(
            "You are meticulous, detail-sensitive and a great marketing strategist. "
            "You also avoid speculation or hallucination. "
            "Work only on the information provided."
        ),
        llm=llm,
        verbose=True,
    )