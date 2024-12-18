Scroll down for English description!
## WiC_decision_maker_model konzolos alkalmazás
Ennek a konzolos alkalmazásnak a feladata, hogy megvizsgálja, hogy a WiC (word in context) feladatot különböző nyelvi modellek mennyire jól tudják megoldani, illetve, hogy mennyire érzékenyek esetlegesen arra, hogyha a 2 példamondatot, amire vonatkozóan döntést kell hozzanak, azt fordított sorrendben adjuk be nekik. Megvizsgált modellek terv szerint gemma2-2b és ennek pár-- a pontosság rovására kisebb méretűvé tett --variánsa, GPT 3.5 és 4, Gemini, és még amire idő jut.

link az adatbázishoz: https://pilehvar.github.io/wic/

link a gemma2-2b-it-t modellhez, méret per minőség arányban egész jó: https://huggingface.co/google/gemma-2-2b-it

Ugyanitt vannak kvantált, azaz a pontosság rovására kisebb méretűvé tett variánsai is ennek a modellnek: https://huggingface.co/models?other=base_model:quantized:google/gemma-2-2b-it

Tudj meg többet a kvantálásról az alábbi linken: https://huggingface.co/docs/optimum/en/concept_guides/quantization illetve https://huggingface.co/docs/hub/en/gguf

A cél, hogy az alkalmazásban a modelleknek alábbi formájú kérdéseket lehessen feltenni:
A és B mondatban ugyanazt jelenti-e az X szó?
Lehetséges platformok erre:
# https://ollama.com/
# https://github.com/vllm-project/vllm
# https://github.com/huggingface/transformers/
# https://github.com/ggerganov/llama.cpp


LLM-k benchmarkjainak összehasonlítása:
# https://llmarena.ai/

## WiC_decision_maker_model console app
The task of this console application is to examine how well different language models can solve the WiC (word in context) task, and how sensitive they might be to the fact that the 2 example sentences for which a decision has to be made are given in reverse order in for them. According to the plan, tested models will be gemma2-2b and its variants - reduced in size at the expense of accuracy, GPT 3.5 and 4, Gemini, and some more as much as time will allow.

link to database: https://pilehvar.github.io/wic/

link to gemma2-2b-it-t model, its size per quality ratio is quite good: https://huggingface.co/google/gemma-2-2b-it

There are also quantized variants of this model (which are smaller at the expense of accuracy) here: https://huggingface.co/models?other=base_model:quantized:google/gemma-2-2b-it

Read about quantization: https://huggingface.co/docs/optimum/en/concept_guides/quantization and https://huggingface.co/docs/hub/en/gguf

The goal is to be able to ask the models the following questions in the application:
Does the word X mean the same thing in sentences A and B? Answer with a single "YES" or "NO".
Possible platforms to do this:





## TODO: 
- Check Large Language Model (LLM) API Playground by Retool
