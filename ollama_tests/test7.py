# This script showcases concurrent generation of responses using the Ollama API.
# It uses two different models with custom temperature and token prediction settings.
# Multiple prompts are processed simultaneously, and the responses are printed.

import asyncio
from ollama import AsyncClient

# Define two different models and their parameters
MODEL_1 = {
    'name': 'llama3.1:latest',
    'temperature': 0.4,
    'num_predict': 150
}

MODEL_2 = {
    'name': 'phi3:medium',
    'temperature': 0.3,
    'num_predict': 150
}

async def generate_response(prompt, model):
    async_client = AsyncClient()
    response = await async_client.generate(
        model=model['name'], 
        prompt=prompt,
        options={
            "temperature": model['temperature'],
            "num_predict": model['num_predict']
        }
    )
    return response['response']

async def chat():
    prompts = [
        'Why is the sky blue?',
        'What is the capital of France?',
        '''Ruminate on how many r's are in the word "barrister"'''
    ]
    
    # Generate responses concurrently for both models
    responses_model1 = await asyncio.gather(*[generate_response(prompt, MODEL_1) for prompt in prompts])
    responses_model2 = await asyncio.gather(*[generate_response(prompt, MODEL_2) for prompt in prompts])
    
    # Print responses for both models
    for i, prompt in enumerate(prompts):
        print(f"Prompt: {prompt}")
        print(f"Response from {MODEL_1['name']}: {responses_model1[i]}")
        print(f"Response from {MODEL_2['name']}: {responses_model2[i]}\n")

if __name__ == "__main__":
    asyncio.run(chat())