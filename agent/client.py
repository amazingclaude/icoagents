from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

from config.settings import AI_FOUNDRY_ENDPOINT, AGENT_NAME, AGENT_VERSION


class ConnectedKerbAgent:
    def __init__(self):
        self.project_client = AIProjectClient(
            endpoint=AI_FOUNDRY_ENDPOINT,
            credential=DefaultAzureCredential(),
        )
        self.openai_client = self.project_client.get_openai_client()

    def ask(self, messages: list[dict[str, str]]) -> str:
        request_messages = [
            {
                "role": message["role"],
                "content": message["content"],
            }
            for message in messages
            if message["role"] in {"user", "assistant"} and message["content"]
        ]

        response = self.openai_client.responses.create(
            input=request_messages,
            extra_body={
                "agent_reference": {
                    "name": AGENT_NAME,
                    "version": AGENT_VERSION,
                    "type": "agent_reference",
                }
            },
        )

        return response.output_text
