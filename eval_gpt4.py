import json
import os
import pandas as pd
from openai import OpenAI
from tqdm import tqdm

INPUT_CSV = "human_validation/evaluator640_test_annotations.csv"
OUTPUT_FILE = "gpt4_outputs.json"
API_MODEL = "gpt-4-0613" 

TASK2PROMPT = {
    "Color Palette Meaning": "GPT4_evaluator_prompts/prompt-colorPaletteMeaning.json",
    "Primary Color Extraction": "GPT4_evaluator_prompts/prompt-primaryColorExtraction.json",
    "Font Extraction": "GPT4_evaluator_prompts/prompt-fontExtraction.json",
    "Font Style": "GPT4_evaluator_prompts/prompt-fontStyle.json",
    "Negative Space Detection": "GPT4_evaluator_prompts/prompt-negativeSpaceDetection.json",
    "Style Classification": "GPT4_evaluator_prompts/prompt-styleClassification.json",
    "Visual Importance": "GPT4_evaluator_prompts/prompt-visualImportance.json",
    "Visual Metaphor": "GPT4_evaluator_prompts/prompt-visualMetaphor.json",
}

def load_context_messages(prompt_path):
    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    with open(prompt_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. System Prompt
    messages = [
        {"role": "system", "content": data['system']}
    ]
    
    # 2. Few-shot Examples (User -> Assistant)
    for q, a in zip(data['user'], data['assistant']):
        messages.append({"role": "user", "content": q})
        messages.append({"role": "assistant", "content": a})
        
    return messages

def get_gpt4_score(client, context_messages, input_query):
    current_messages = context_messages + [{"role": "user", "content": input_query}]

    try:
        response = client.chat.completions.create(
            model=API_MODEL,
            messages=current_messages,
            temperature=0.0,
            top_p=1.0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"API Error: {e}")
        return "Error"


if __name__ == "__main__":
    if "OPENAI_API_KEY" not in os.environ:
        print("Warning: OPENAI_API_KEY environment variable not set.")

    client = OpenAI() 

    print(f"Loading data from {INPUT_CSV}...")
    df = pd.read_csv(INPUT_CSV)
    
    results = []
    
    print(f"Starting evaluation on {len(df)} samples with model {API_MODEL}...")
    
    for idx, row in tqdm(df.iterrows(), total=len(df)):
        task_name = row.get('task_category')
        input_query = row.get('input_query')
        
        prompt_file = TASK2PROMPT.get(task_name)
        
        if not prompt_file:
            print(f"Skipping row {idx}: Unknown task '{task_name}'")
            continue
            
        context = load_context_messages(prompt_file)
        
        gpt_output = get_gpt4_score(client, context, input_query)
        
        results.append({
            "sample_id": idx,
            "task_category": task_name,
            "input_query": input_query,
            "gpt4_output": gpt_output
        })

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
        
    print(f"\nSuccess! Results saved to {OUTPUT_FILE}")