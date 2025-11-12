import json
import httpx

from agno.agent import Agent
from agno.models.llama_cpp import LlamaCpp 


def get_top_hackernews_stories(num_stories: int = 10) -> str:
    """
    Use this function to get top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of top stories.
    """

    # Fetch top story IDs from the Hacker News API
    response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    # Parse JSON list of story IDs
    story_ids = response.json()

    # Prepare container for story details
    stories = []
    # Loop over the first `num_stories` IDs and fetch each story's data
    for story_id in story_ids[:num_stories]:
        # Request the story/item details by ID
        story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        # Parse the story JSON payload
        story = story_response.json()
        # Remove 'text' if present to avoid including long HTML/text content in the result
        if "text" in story:
            story.pop("text", None)
        # Add the cleaned story dict to the list
        stories.append(story)
    # Return the collected stories as a JSON-formatted string
    return json.dumps(stories)

agent = Agent(
    model=LlamaCpp(id="ggml-org/gpt-oss-20b-GGUF"),
    tools=[get_top_hackernews_stories],
    markdown=True)

agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)