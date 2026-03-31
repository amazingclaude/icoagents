from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from config.settings import (
    AI_FOUNDRY_ENDPOINT,
    AGENT_NAME,
    AGENT_VERSION,
)

class ConnectedKerbAgent:
    def __init__(self):
        self.project_client = AIProjectClient(
            endpoint=AI_FOUNDRY_ENDPOINT,
            credential=DefaultAzureCredential(),
        )
        self.openai_client = self.project_client.get_openai_client()

    def ask(self, user_message: str) -> str:
        response = self.openai_client.responses.create(
            input=[
                {"role": "user", "content": user_message}
            ],
            extra_body={
                "agent_reference": {
                    "name": AGENT_NAME,
                    "version": AGENT_VERSION,
                    "type": "agent_reference"
                }
            },
        )

        return response.output_text