import argparse
from .hello_crew import run
from .application.features.input.crew import run_input_feature

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
    result = run_input_feature(inp=prompt)
    print(result)

if __name__ == "__main__":
    main()