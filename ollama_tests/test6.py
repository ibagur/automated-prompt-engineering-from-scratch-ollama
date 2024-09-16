# This script showcases concurrent generation of responses using the Ollama API.
# It uses an existing Ollama model with custom temperature and token prediction settings.
# Multiple prompts are processed simultaneously, and the responses are printed.

import asyncio
from ollama import AsyncClient

MODEL_NAME = 'llama3.1:latest'
TEMPERATURE = 0  # You can adjust this value as needed
NUM_PREDICT = 100  # You can adjust this value as needed

async def generate_response(prompt):
    async_client = AsyncClient()
    response = await async_client.generate(
        model=MODEL_NAME, 
        prompt=prompt,
        options={
            "temperature": TEMPERATURE,
            "num_predict": NUM_PREDICT
        }
    )
    return response['response']

async def chat():
    prompts = [
        'Why is the sky blue?',
        'What is the capital of France?',
        'How do plants photosynthesize?'
    ]
    
    # Generate responses concurrently
    responses = await asyncio.gather(*[generate_response(prompt) for prompt in prompts])
    
    # Print responses
    for prompt, response in zip(prompts, responses):
        print(f"Prompt: {prompt}")
        print(f"Response: {response}\n")

if __name__ == "__main__":
    asyncio.run(chat())