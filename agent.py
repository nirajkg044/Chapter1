from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

AGENT_MODEL = "gemini-2.5-flash"


def get_review_sentiment(phoneBrand: str) -> dict:
    """Retrieves the customer sentiment for a specified phone brand.

    Args:
        phoneBrand (str): The name of the phone brand (e.g., "iPhone", "Samsung", "Google Pixel").

    Returns:
        dict: A dictionary containing the phone brand sentiment information.
              Includes a 'review' key ('excellent', 'good', or 'neutral').
              If 'excellent', includes a 'report' key with most favorite features details.
              If 'good', includes  a 'report' key with most likely features details.             
              If 'neutral', includes a 'report' key with common feature details.             
    """
    print(f"--- Tool: get_review_sentiment called for phone brand: {phoneBrand} ---")  # Log tool execution
    phoneBrand_normalized = phoneBrand.lower().replace(" ", "")  # Basic normalization

    # Mock Phone Review data
    # api call
    mock_phoneBrand_db = {
        "iPhone": {
            "review": "excellent",
            "report": "In 2026, the iPhone 17 is widely reviewed as the best choice for most users, offering premium features like a 120Hz ProMotion display and great battery at a standard price.",
        },
        "Samsung": {
            "review": "good",
            "report": "The Samsung Galaxy S26 Ultra is widely reviewed as the best smartphone of early 2026, offering a 200MP camera, advanced AI features, and bright screen and top-tier performance.",
        },
        "Google Pixel": {
            "review": "neutral",
            "report": "In early 2026, the best Google Pixel phones are the Pixel 10 Pro XL for top-tier performance with Tensor G5, and the Pixel 9a as the best budget pick, praised for its value and AI capabilities."
        },
    }


    if phoneBrand_normalized in mock_phoneBrand_db:
        return mock_phoneBrand_db[phoneBrand_normalized]
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have review information for '{phoneBrand}'.",
        }



root_agent = Agent(
    name = "L1triageAgent",
    # model = LiteLlm(AGENT_MODEL),
    model = AGENT_MODEL,
    description = "An agent that take phone brand e.g. iPhone as input and share the customer review with excellent, good, neutral."
    #instructions = "You are a helpful travel planner assistant. You can assist users in finding and booking flights, hotels, and activities for their trips. Always provide clear and concise information, and ask follow-up questions if you need more details to better assist the user."
    tools=[get_review_sentiment]
)
