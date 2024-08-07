import os
from dotenv import load_dotenv
import schemathesis
from schemathesis.cli import run

# Load environment variables from the .env file
load_dotenv()

# Use the base URL of your running Flask app
schema = schemathesis.from_path("openapi.yaml", base_url="https://improved-waddle-4vjj97p6wj5f77jr-5000.app.github.dev")

@schema.parametrize()
def test_api(case):
    response = case.call()
    case.validate_response(response)

if __name__ == "__main__":
    # Run the tests
    results = run([__file__])

    # Get the API key from the environment variable
    api_key = os.getenv("SCHEMATHESIS_API_KEY")
    if not api_key:
        raise ValueError("API key is not set. Please set the SCHEMATHESIS_API_KEY environment variable.")

    # Upload results to Schemathesis.io
    results.upload(api_key)
