#https://docs.agno.com/agent-os/introduction

from agno.models.llama_cpp import LlamaCpp
from agno.agent import Agent
from agno.tools.mcp import MCPTools
from agno.db.sqlite import SqliteDb
from agno.os import AgentOS

from dotenv import load_dotenv
load_dotenv()

assistant = Agent(
    model=LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
    # Add a database to the Agent
    db=SqliteDb(db_file="agno.db"),
    tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
    # Add the previous session history to the context
    add_history_to_context=True,
    markdown=True
)


agent_os = AgentOS(
    id="my-first-os",
    description="My first AgentOS",
    agents=[assistant],
)

app = agent_os.get_app()

if __name__ == "__main__":
    # Default port is 7777; change with port=...
    agent_os.serve(app="agno_os_doc:app", reload=True)


# uv run python3 agno_os_doc.py -> http://localhost:7777