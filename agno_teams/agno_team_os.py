from agno.team import Team
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
from agno.models.llama_cpp import LlamaCpp 
from agno.os import AgentOS #https://docs.agno.com/agent-os/introduction
from agno.db.sqlite import SqliteDb

from dotenv import load_dotenv
import os
load_dotenv()  # Load variables from .env file

# Now use the key
groq_api_key = os.getenv("GROQ_API_KEY")

# Create specialized agents
news_agent = Agent(
    id="news-agent",
    name="News Agent",
    role="Get the latest news and provide summaries",
    tools=[TavilyTools()]
)

weather_agent = Agent(
    id="weather-agent",
    name="Weather Agent",
    role="Get weather information and forecasts",
    tools=[TavilyTools()]
)

# Create the team
team = Team(
    name="News and Weather Team",
    # Add a database to the Agent
    db=SqliteDb(db_file="agno.db"),
    #model=Groq(id="openai/gpt-oss-20b"),
    model=LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
    members=[news_agent, weather_agent],
    #model=OpenAIChat(id="gpt-4o"),
    instructions="Coordinate with team members to provide comprehensive information. Delegate tasks based on the user's request.",
    markdown=True
)

agent_os = AgentOS(teams=[team])
app = agent_os.get_app()

# uv run fastapi dev agno_team_os.py

#current time and weather of helsinki
# What's the latest news and weather in Tokyo?