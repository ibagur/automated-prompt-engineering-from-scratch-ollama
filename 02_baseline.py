import asyncio
import pandas as pd
from prompt_evaluator import PromptEvaluator


if __name__ == "__main__":
    df_train = pd.read_csv('test.csv')  # Load your training data

    target_model_config = {
        'name': 'gemma2:latest',
        'temperature': 0,
        'num_predict': 1000
    }

    review_model_config = {
        'name': 'deepseek-coder-v2:latest',
        'temperature': 0,
        'num_predict': 10
    }

    review_prompt_template_path = 'review_prompt_template.txt'  # Path to the review prompt text file

    evaluator = PromptEvaluator(
        df_train, target_model_config, review_model_config, review_prompt_template_path
    )
    
    prompt = input("Please enter the prompt for evaluation: ")
    asyncio.run(evaluator.main(prompt))