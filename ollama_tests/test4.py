# This script demonstrates sequential question-answering using the Ollama API.
# It asks a series of predefined questions one after another, measures the total time taken,
# and prints both the questions and answers along with the execution time.

import asyncio
import time
from ollama import AsyncClient

async def ask_question(client, question):
    message = {'role': 'user', 'content': question}
    try:
        response = await client.chat(model='phi3:medium', messages=[message])
        return f"Q: {question}\nA: {response['message']['content']}\n"
    except Exception as e:
        return f"Error for '{question}': {str(e)}\n"

async def sequential_chat():
    client = AsyncClient()
    
    questions = [
        "Why is the sky blue?",
        "What is the capital of France?",
        "How does photosynthesis work?",
        "What is the theory of relativity?",
        "Who wrote 'Romeo and Juliet'?"
    ]
    
    print("Asking questions sequentially...\n")
    
    start_time = time.time()  # Start the timer
    
    # Ask questions sequentially
    for question in questions:
        result = await ask_question(client, question)
        print(result)
    
    end_time = time.time()  # Stop the timer
    duration = end_time - start_time  # Calculate duration
    
    print(f"\nTotal time taken: {duration:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(sequential_chat())