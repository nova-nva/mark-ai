from crewai import Agent

def build_input_parser(llm=None) -> Agent:
    """
    Role: Human Input Analyst
    Goal: Analyze user input, get the mandatory points and proceed or terminate if criticial info is not provided
    Inputs: {prompt}
    Output: Structured list with clear points  
    """
    return Agent (
        role="Human Input Analyst",
        goal="Analyze, standarize and validate user input: {prompt} and produce a structured response",
        backstory=(
            "You are meticulous, observative and avoid speculation or hallucination"
            "Focus only on the information provided. If specific critical points are not provided, do not try to infere them."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )