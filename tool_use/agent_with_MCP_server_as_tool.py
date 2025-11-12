# https://docs.agno.com/concepts/tools/mcp/overview
# uv add mcp

from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.mcp import MCPTools


from agno.models.llama_cpp import LlamaCpp

mcp_tools = MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")

agent = Agent(
    model=LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
    tools=[mcp_tools],
    markdown=True
)


agent.print_response("What is AgentOS in Agno", stream=True)
