# #https://docs.agno.com/agent-os/introduction
# uv add 'fastapi[standard]' sqlalchemy

from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.hackernews import HackerNewsTools
from agno.tools.mcp import MCPTools
from agno.db.sqlite import SqliteDb
from agno.os import AgentOS #https://docs.agno.com/agent-os/introduction

from dotenv import load_dotenv
load_dotenv()

from agno.models.llama_cpp import LlamaCpp 

agno_agent = Agent(
    model=LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
    # Add a database to the Agent
    db=SqliteDb(db_file="agno.db"),
    #tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
    tools=[HackerNewsTools()],
    # Add the previous session history to the context
    add_history_to_context=True,
    markdown=True
)

""" agent = Agent(
    model=OpenAIChat(id="gpt-5-mini"),
    #tools = [HackerNewsTools()],
    tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
    markdown=True
) """



# Create the AgentOS
agent_os = AgentOS(agents=[agno_agent])
# Get the FastAPI app for the AgentOS

app = agent_os.get_app()

# run the following in terminal -> port 8000
# uv run fastapi dev agno_os_tools.py


# connect to AgentOS UI
# https://os.agno.com/

#################

# 3. Serve it
""" app = agent_os.get_app()
if __name__ == "__main__":
    agent_os.serve(app="agno_os_tools:app", reload=True) """
    
    
# uv run python3 agno_os_tools.py -> port 7777
