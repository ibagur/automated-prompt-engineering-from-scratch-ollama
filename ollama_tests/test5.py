# This script creates a custom model based on 'phi3:medium' with specific parameters,
# uses it to generate responses to multiple prompts concurrently,
# and then deletes the custom model after use.

import asyncio
from ollama import Client,AsyncClient

MODEL_NAME = 'example'

modelfile='''
FROM phi3:medium
PARAMETER temperature 0
PARAMETER num_predict 100
'''

def create_model():
    client = Client()
    print(f"Creating custom model '{MODEL_NAME}'...")
    client.create(model=MODEL_NAME, modelfile=modelfile)
    print(f"Model '{MODEL_NAME}' created successfully.")

def delete_model():
    client = Client()
    print(f"Deleting model '{MODEL_NAME}'...")
    client.delete(model=MODEL_NAME)
    print(f"Model '{MODEL_NAME}' deleted successfully.")

async def generate_response(prompt):
    async_client = AsyncClient()
    response = await async_client.generate(model=MODEL_NAME, prompt=prompt)
    return response['response']

async def chat():
    # Create the model synchronously (only needs to be done once)
    create_model()
    
    try:
        # Example of handling multiple concurrent requests
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
    finally:
        # Delete the model after we're done, even if an error occurred
        delete_model()

if __name__ == "__main__":
    asyncio.run(chat())
