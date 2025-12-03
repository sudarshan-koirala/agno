from agno.team import Team
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
from agno.models.llama_cpp import LlamaCpp 
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
    model=Groq(id="openai/gpt-oss-20b"),
    #model=LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
    members=[news_agent, weather_agent],
    #model=OpenAIChat(id="gpt-4o"),
    instructions="Coordinate with team members to provide comprehensive information. Delegate tasks based on the user's request."
)

#team.print_response("What's the latest news and weather in Tokyo?", stream=True)

################ STREAM RESPONSE #################
stream = team.run("What's the latest news and weather in Tokyo?", stream=True)
for chunk in stream:
    print(chunk.content, end="", flush=True)