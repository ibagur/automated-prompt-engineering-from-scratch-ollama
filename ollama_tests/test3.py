# This script demonstrates concurrent question-answering using the Ollama API.
# It processes multiple predefined questions simultaneously, measures the total time taken,
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

async def concurrent_chat():
    client = AsyncClient()
    
    questions = [
        "Why is the sky blue?",
        "What is the capital of France?",
        "How does photosynthesis work?",
        "What is the theory of relativity?",
        "Who wrote 'Romeo and Juliet'?"
    ]
    
    print("Asking multiple questions concurrently...\n")
    
    start_time = time.time()  # Start the timer
    
    # Create tasks for each question
    tasks = [ask_question(client, q) for q in questions]
    
    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()  # Stop the timer
    duration = end_time - start_time  # Calculate duration
    
    # Print results
    for result in results:
        print(result)
    
    print(f"\nTotal time taken: {duration:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(concurrent_chat())