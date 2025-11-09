# install ipykernel and run interactive window ( Shift + Enter)
from agno.agent import Agent

#Agent??

# check my latest video about llama.cpp https://youtu.be/HX1wUis68GQ?si=nvBCCS0WeAJ7kJPW
# agno doc https://docs.agno.com/concepts/models/llama_cpp
# need to also install openai package 

from agno.models.llama_cpp import LlamaCpp 

agent = Agent(
    model=LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
    markdown=True
)

# Print the response in the terminal
# if you want to run from interactive window, install ipywidgets
#agent.print_response("Share 2 sentences about Nepal.")



################# Using OpenAI models #################

# Open source models are good but sometimes it takes ages to run
# answer are also not that good when using agentic use cases.abs

# update the .env with api keys
# get keys from here https://platform.openai.com/account/api-keys
from dotenv import load_dotenv
load_dotenv()

from agno.models.openai import OpenAIChat
from agno.agent import Agent

agent = Agent(
    model=OpenAIChat(id="gpt-5-mini"),
    markdown=True
)

#agent.run("Share 2 sentences about Nepal")
agent.print_response("Share 2 sentences about Nepal.")
