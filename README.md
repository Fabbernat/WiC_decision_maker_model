# WiC_decision_maker_model
Az alkalmazás megvizsgálja, hogy a WiC (word in context) feladatot különböző nyelvi modellek mennyire jól tudják megoldani, illetve, hogy mennyire érzékenyek esetlegesen arra, hogyha a 2 példamondatot, amire vonatkozóan döntést kell hozzanak, azt fordított sorrendben adjuk be nekik. Megvizsgált modellek terv szerint gemma2-2b és ennek pár-- a pontosság rovására kisebb méretűvé tett --variánsa, GPT 3.5 és 4, Gemini, és még amire idő jut.

adatbázis: https://pilehvar.github.io/wic/

gemma2-2b-it-t modell, méret/minőség arányban egész jó: https://huggingface.co/google/gemma-2-2b-it
Ugyanitt vannak kvantált (a pontosság rovására kisebb méretűvé tett) variánsai is ennek a modellnek: https://huggingface.co/models?other=base_model:quantized:google/gemma-2-2b-it
Olvass majd utána a kvantálásnak is: https://huggingface.co/docs/optimum/en/concept_guides/quantization illetve https://huggingface.co/docs/hub/en/gguf

A cél, hogy az alkalmazásban a modelleknek alábbi formájú kérdéseket lehessen feltenni:
A és B mondatban ugyanazt jelenti-e az X szó?
Lehetséges platformok erre:
# https://ollama.com/
# https://github.com/vllm-project/vllm
# https://github.com/huggingface/transformers/
# https://github.com/ggerganov/llama.cpp


LLM-k benchmarkjainak összehasonlítása:
# https://llmarena.ai/
