from crewai import Agent
from crewai_tools import SerperDevTool

def build_researcher(llm=None) -> Agent:
    return Agent (
        role="Marketing Strategy Expert",
        goal="Detect the missing points (the ones marked with None) research about the best Brand Tone and Social Media Platform target to launch our marketing campaign",
        backstory=(
            "You are meticulous, detail-sensitive and a great marketing strategist. "
            "You also avoid speculation or hallucination. "
            "Work only on the information provided."
        ),
        llm=llm,
        verbose=True,
    )

def build_tendency_researcher(llm=None) -> Agent:
    return Agent (
        role="Social Media Trends Expert",
        goal="Research about the actual tendencies and trends in Social Media networks based on the input provided. ",
        backstory=(
            "You are really curious and you are up-to-date with the last tendencies, trends, movements in high-engagement social media (Instragram, Facebook, LinkedIn, TikTok). "
            "You also avoid speculation or hallucination. "
            "Base your research on the information provided. "
        ),
        tools=[SerperDevTool()],
        llm=llm,
        verbose=True,
    )