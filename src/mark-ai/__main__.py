import argparse
import agentops
import os

from .application.flows.run import run_flow

def main():
    parser = argparse.ArgumentParser(prog="mark-ai", description="CLI for Crew Execution")
    parser.add_argument(
        "-p", "--prompt",
        type=str,
        help="Prompt for Mark AI to solve",
    )
    args = parser.parse_args()

    # receive and execute prompt
    prompt = args.prompt or "Greet and kindly ask for instructions in a sentence."
    result = run_flow(user_input=prompt)
    print(result)

if __name__ == "__main__":
    agentops.init(os.getenv("AGENT_OPS_API_KEY"))
    main()