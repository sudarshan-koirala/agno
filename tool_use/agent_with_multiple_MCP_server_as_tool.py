# https://docs.agno.com/concepts/tools/mcp/overview
# uv add mcp

import asyncio
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.mcp import MCPTools


from agno.models.llama_cpp import LlamaCpp


async def run_agent(message: str) -> None:
    """Run the Airbnb and Google Maps agent with the given message."""

    # Initialize and connect to multiple MCP servers
    mcp_airbnb_tools = MCPTools(command="npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")

    mcp_tools_agno_doc = MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp", tool_name_prefix="dev")
    
    await mcp_airbnb_tools.connect()

    try:
        agent = Agent(
            model=LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
            tools=[mcp_airbnb_tools, mcp_tools_agno_doc],
            markdown=True,
        )

        await agent.aprint_response(message, stream=True)
    finally:
        await mcp_airbnb_tools.close()


# Example usage
if __name__ == "__main__":
    # Pull request example
    asyncio.run(
        run_agent(
            #"Find 2 listings that are available in Helsinki for 2 people for 3 nights from 1 to 4 December 2025?"
            "What is Agno ?"
        )
    )