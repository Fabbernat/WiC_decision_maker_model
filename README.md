### Scroll down for English description!

# Peternity konzolos és webalkalmazás
Ennek a konzolos és web alkalmazásnak a feladata, hogy megvizsgálja, hogy a WiC (word in context) feladatot különböző nyelvi modellek mennyire jól tudják megoldani, illetve, hogy mennyire érzékenyek esetlegesen arra, hogyha a 2 példamondatot, amire vonatkozóan döntést kell hozzanak, azt fordított sorrendben adjuk be nekik. Az alkalmazás tartalmaz egy szkriptet is, amely képes a legtöbb magyar szót helyesen elválasztani. A modul kifejezetten a magyar elválasztási szabályok figyelembevételével készült.

## Megvizsgált algoritmusok és  modellek terv szerint:
* gemma2-2b és ennek pár-- a pontosság rovására kisebb méretűvé tett --variánsa.
* GPT-Neo: A GPT-3 egy nyílt forráskódú változata.
* OPT: A Facebook által fejlesztett nagy nyelvi modell.
* BLOOM: A BigScience projekt által fejlesztett többnyelvű LLM.
*  ... és még amire idő jut.


## Linkek
- Link az adatbázishoz: https://pilehvar.github.io/wic/

- Link a gemma2-2b-it-t modellhez, méret per minőség arányban egész jó: https://huggingface.co/google/gemma-2-2b-it

- Ugyanitt vannak **kvantált**, azaz **a pontosság rovására kisebb méretűvé tett** variánsai is ennek a modellnek: https://huggingface.co/models?other=base_model:quantized:google/gemma-2-2b-it

- Tudj meg többet a kvantálásról az alábbi linken: https://huggingface.co/docs/optimum/en/concept_guides/quantization illetve https://huggingface.co/docs/hub/en/gguf

## A cél, hogy az alkalmazásban a modelleknek alábbi formájú kérdéseket lehessen feltenni:
A és B mondatban ugyanazt jelenti-e az X szó?
## Lehetséges platformok erre:
### https://ollama.com/
### https://github.com/vllm-project/vllm
### https://github.com/huggingface/transformers/
### https://github.com/ggerganov/llama.cpp

## Magyar nyelvű magyarázó videó hozzá:
https://www.inf.u-szeged.hu/~rfarkas/NLP/ - 5. hét - Jelentésegyértelműsítés 

## LLM-k benchmarkjainak összehasonlítása:
### https://llmarena.ai/

## TESZTELÉS:
- Check Large Language Model (LLM) API Playground by Retool
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# English version:

# Peternity console and web app
The task of this console and web application is to examine how well different language models can solve the WiC (word in context) task, and how sensitive they might be to the fact that the 2 example sentences for which a decision has to be made are given in reverse order in for them. The app also has a script that can hyphenate most Hungarian words correctly. The module is specifically designed for Hungarian hyphenation rules.

## According to the plan, tested models will be:
*  gemma2-2b and its variants - reduced in size at the expense of accuracy, GPT 3.5 and 4, Gemini,
* GPT-Neo
* OPT
* BLOOM
*  and some more as much as time will allow.

## Links
- Link to database: https://pilehvar.github.io/wic/

- Link to gemma2-2b-it-t model, its size per quality ratio is quite good: https://huggingface.co/google/gemma-2-2b-it

- There are also quantized variants of this model (which are smaller at the expense of accuracy) here: https://huggingface.co/models?other=base_model:quantized:google/gemma-2-2b-it

- Read about quantization: https://huggingface.co/docs/optimum/en/concept_guides/quantization and https://huggingface.co/docs/hub/en/gguf

## The goal is to be able to ask the models the following questions in the application:
Does the word X mean the same thing in sentences A and B? Answer with a single "YES" or "NO".
Possible platforms to do this:
### https://ollama.com/
### https://github.com/vllm-project/vllm
### https://github.com/huggingface/transformers/
### https://github.com/ggerganov/llama.cpp

## Hungarian explanatory video:
https://www.inf.u-szeged.hu/~rfarkas/NLP/ – Week 5 – Word Sense Disambiguation

## Compare benchmarks of LLM's:
### https://llmarena.ai/

## TESTING:
- Check Large Language Model (LLM) API Playground by Retool
