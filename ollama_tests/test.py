# This script demonstrates a simple chat interaction using the Ollama API.
# It sends a predefined question to the 'phi3:medium' model and prints the response.

import asyncio
from ollama import AsyncClient

async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  response = await AsyncClient().chat(model='phi3:medium', messages=[message])
  print(response['message']['content'])

if __name__ == "__main__":
    asyncio.run(chat())