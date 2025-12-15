# https://docs.agno.com/basics/workflows/overview
from agno.agent import Agent
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
from agno.models.llama_cpp import LlamaCpp 
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
import os
load_dotenv()  # Load variables from .env file
# Now use the key
groq_api_key = os.getenv("GROQ_API_KEY")


# Define agents with specific roles
researcher = Agent(
    name="Researcher",
    model=Groq(id="openai/gpt-oss-20b"),
    #model=LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"
    instructions="Find relevant information about the topic",
    tools=[TavilyTools()]
)

writer = Agent(
    name="Writer",
    model=Groq(id="openai/gpt-oss-20b"),
    #model=LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"
    instructions="Write a clear, engaging article based on the research"
)

# Chain them together in a workflow
content_workflow = Workflow(
    name="Content Creation",
    db=SqliteDb(db_file="tmp/content_workflow.db"),
    steps=[researcher, writer],
)

# Run the workflow
content_workflow.print_response("Write an article about climate change solutions", stream=True)