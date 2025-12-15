# https://docs.agno.com/basics/workflows/workflow-patterns/branching-workflow
from typing import List

from agno.agent.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.tavily import TavilyTools
from agno.workflow.router import Router
from agno.workflow.step import Step
from agno.workflow.types import StepInput
from agno.workflow.workflow import Workflow
from agno.models.groq import Groq
from agno.models.llama_cpp import LlamaCpp 
from agno.db.sqlite import SqliteDb
from agno.os import AgentOS #https://docs.agno.com/agent-os/introduction
from agno.tracing import setup_tracing #https://docs.agno.com/basics/tracing/overview
from dotenv import load_dotenv
import os
load_dotenv()  # Load variables from .env file

db = SqliteDb(db_file="tmp/traces.db")

# Now use the key
groq_api_key = os.getenv("GROQ_API_KEY")

# Define the research agents
hackernews_agent = Agent(
    name="HackerNews Researcher",
    #model=Groq(id="openai/gpt-oss-20b"),
    model = LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
    instructions="You are a researcher specializing in finding the latest tech news and discussions from Hacker News. Focus on startup trends, programming topics, and tech industry insights.",
    tools=[HackerNewsTools()],
)

web_agent = Agent(
    name="Web Researcher",
    #model=Groq(id="openai/gpt-oss-20b"),
    model = LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
    instructions="You are a comprehensive web researcher. Search across multiple sources including news sites, blogs, and official documentation to gather detailed information.",
    tools=[TavilyTools()],
)

content_agent = Agent(
    name="Content Publisher",
    #model=Groq(id="openai/gpt-oss-20b"),
    model = LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
    instructions="You are a content creator who takes research data and creates engaging, well-structured articles. Format the content with proper headings, bullet points, and clear conclusions.",
)

# Create the research steps
research_hackernews = Step(
    name="research_hackernews",
    agent=hackernews_agent,
    description="Research latest tech trends from Hacker News",
)

research_web = Step(
    name="research_web",
    agent=web_agent,
    description="Comprehensive web research on the topic",
)

publish_content = Step(
    name="publish_content",
    agent=content_agent,
    description="Create and format final content for publication",
)


# Now returns Step(s) to execute
def research_router(step_input: StepInput) -> List[Step]:
    """
    Decide which research method to use based on the input topic.
    Returns a list containing the step(s) to execute.
    """
    # Use the original workflow message if this is the first step
    topic = step_input.previous_step_content or step_input.input or ""
    topic = topic.lower()

    # Check if the topic is tech/startup related - use HackerNews
    tech_keywords = [
        "startup",
        "programming",
        "ai",
        "machine learning",
        "software",
        "developer",
        "coding",
        "tech",
        "silicon valley",
        "venture capital",
        "cryptocurrency",
        "blockchain",
        "open source",
        "github",
    ]

    if any(keyword in topic for keyword in tech_keywords):
        print(f"🔍 Tech topic detected: Using HackerNews research for '{topic}'")
        return [research_hackernews]
    else:
        print(f"🌐 General topic detected: Using web research for '{topic}'")
        return [research_web]


workflow = Workflow(
    name="Intelligent Research Workflow",
    description="Automatically selects the best research method based on topic, then publishes content",
    steps=[
        Router(
            name="research_strategy_router",
            selector=research_router,
            choices=[research_hackernews, research_web],
            description="Intelligently selects research method based on topic",
        ),
        publish_content,
    ],
    db=db
)

agent_os = AgentOS(workflows=[workflow], tracing=True)
app = agent_os.get_app()

# uv run fastapi dev agno_branching_workflow_agentOS_traces.py

# Latest developments in artificial intelligence and machine learning