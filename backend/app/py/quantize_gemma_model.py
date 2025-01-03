from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def quantize_gemma_model(model_name: str, quantization_type: str = '8bit'):
    """
    Load and quantize the Gemma model.
    
    Args:
        model_name (str): The Hugging Face model identifier.
        quantization_type (str): Type of quantization ('8bit' or '4bit').
    
    Returns:
        model: The quantized model.
        tokenizer: The tokenizer associated with the model.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    if quantization_type == '8bit':
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map='auto',
            load_in_8bit=True,
            torch_dtype=torch.float16
        )
    elif quantization_type == '4bit':
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map='auto',
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16
        )
    else:
        raise ValueError("Unsupported quantization type. Choose '8bit' or '4bit'.")
    
    return model, tokenizer

def evaluate_wic_task(model, tokenizer, sentence1: str, sentence2: str, target_word: str):
    """
    Evaluate the WiC (Word in Context) task using the given model.
    
    Args:
        model: The language model.
        tokenizer: The tokenizer associated with the model.
        sentence1 (str): First sentence containing the target word.
        sentence2 (str): Second sentence containing the target word.
        target_word (str): The ambiguous word to evaluate.
    
    Returns:
        result: Model's prediction on whether the target word has the same meaning in both sentences.
    """
    prompt = (
        f"Does the word '{target_word}' have the same meaning in the following sentences?\n"
        f"Sentence A: {sentence1}\n"
        f"Sentence B: {sentence2}\n"
        "Answer with 'Yes' or 'No'."
    )
    inputs = tokenizer(prompt, return_tensors='pt').to('cuda')
    output = model.generate(**inputs, max_length=10)
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return result

if __name__ == '__main__':
    MODEL_NAME = 'google/gemma-2b-it'
    QUANTIZATION_TYPE = '8bit'  # Change to '4bit' if needed
    
    model, tokenizer = quantize_gemma_model(MODEL_NAME, QUANTIZATION_TYPE)
    print(f"Model {MODEL_NAME} loaded and quantized with {QUANTIZATION_TYPE}.")
    
    # WiC Task Example
    sentence1 = "He went to the bank to deposit money."
    sentence2 = "She sat on the river bank and enjoyed the view."
    target_word = "bank"
    
    result = evaluate_wic_task(model, tokenizer, sentence1, sentence2, target_word)
    print(f"WiC Task Result: {result}")
    
    # Reverse Sentence Order Test
    result_reversed = evaluate_wic_task(model, tokenizer, sentence2, sentence1, target_word)
    print(f"WiC Task Result (Reversed Order): {result_reversed}")