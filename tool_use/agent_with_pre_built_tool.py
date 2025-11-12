# Tools are functions your Agno Agents can use to get things done.

# https://docs.agno.com/concepts/tools/overview

from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.hackernews import HackerNewsTools

from dotenv import load_dotenv
load_dotenv()

from agno.models.llama_cpp import LlamaCpp 

agent = Agent(
    model=LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
    tools = [HackerNewsTools()],
    markdown=True
)

agent.print_response("List 5 trending startups and products.", stream=True)
