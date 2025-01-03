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

if __name__ == '__main__':
    MODEL_NAME = 'google/gemma-2b-it'
    QUANTIZATION_TYPE = '8bit'  # Change to '4bit' if needed
    
    model, tokenizer = quantize_gemma_model(MODEL_NAME, QUANTIZATION_TYPE)
    print(f"Model {MODEL_NAME} loaded and quantized with {QUANTIZATION_TYPE}.")
    
    # Test inference
    input_text = "Explain the benefits of quantization in AI models."
    inputs = tokenizer(input_text, return_tensors='pt').to('cuda')
    output = model.generate(**inputs, max_length=50)
    print(tokenizer.decode(output[0], skip_special_tokens=True))
