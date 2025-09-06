from crewai import Agent, Task, Crew, LLM
import os

def _gemini_llm():
    # config
    return LLM(
        model="gemini/gemini-1.5-flash",
        api_key = os.getenv("GEMINI API KEY"),
        temperature=0.2
    )


def run(prompt: str):
    llm = _gemini_llm()

    # test minimun agent
    greeter = Agent(
        role="Greeter",
        goal="Give a one sentence response over the task asked from the PM",
        backstory="Your name is MarAI. You are useful, clear and direct.",
        verbose=True,
        llm=llm
    )

    # minimum task
    hello_task = Task(
        description=prompt,
        expected_output="A single kind sentence",
        agent=greeter,
        llm=llm
    )

    crew = Crew(agents=[greeter], tasks=[hello_task], llm=llm)
    result = crew.kickoff()
    print(result)
    return result