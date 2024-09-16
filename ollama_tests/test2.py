# This script implements an interactive chat interface using the Ollama API.
# It allows users to have a conversation with an AI model ('phi3:medium'),
# continuing until the user types 'exit' to end the session.

import asyncio
from ollama import AsyncClient

async def chat():
    client = AsyncClient()
    
    print("Welcome to the AI chat! Type 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Create message dictionary
        message = {'role': 'user', 'content': user_input}
        
        # Make API call
        try:
            response = await client.chat(model='phi3:medium', messages=[message])
            print("AI:", response['message']['content'])
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(chat())