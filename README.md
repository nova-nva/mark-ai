# Mark AI

## How to run
1. Clone the repo. 
2. Config env variables: 
- GEMINI_API_KEY
- SERPER_API_KEY
- AGENTOPS_API_KEY
3. With UV (if you don't have UV, skip to step 4)
- $ uv venv
- $ uv sync
- $ uv run -m mark-ai --prompt "some prompt"

4. With PIP (linux/WSL)
- $ python3 -m venv .venv
- $ source .venv/bin/activate
- $ python -m pip install --upgrade pip
- $ pip install -r requirements.txt
- $ python -m mark_ai --prompt "some prompt"

## Tools used:
1. UV: dependency management (optimized than pip)
- $ uv venv
2. Crew AI
3. AgentOps

## Improvement points
1. Go with multi-crew partitions
2. Provide brand info for the agents to consume via RAG
