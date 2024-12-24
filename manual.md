# Manual how to use this app
1. Visit https://ollama.com/download and download the installer file (https://ollama.com/download/OllamaSetup.exe for Windows)
2. Follow the steps of the installer and install Ollama
3. Open a terminal and type the following commands:
   - `ollama run llama3` - this may take several minutes
   - You should see a darkgray placeholder hint message: `Send a message (/? for hel
4. We have this database:
```
Answer with a single "YES" or "NO"!
Does the word "defeat" mean the same in sentence "It was a narrow defeat ." as in sentence"The army 's only defeat ."?
Does the word "groom" mean the same in sentence "Groom the dogs ." as in sentence"Sheila groomed the horse ."?
Does the word "penetration" mean the same in sentence "The penetration of upper management by women ." as in sentence"Any penetration , however slight , is sufficient to complete the offense ."?
Does the word "hit" mean the same in sentence "We hit Detroit at one in the morning but kept driving through the night ." as in sentence"An interesting idea hit her ."?
Does the word "deliberation" mean the same in sentence "He was a man of judicial deliberation ." as in sentence"A little deliberation would have deterred them ."?
Does the word "navel" mean the same in sentence "They argued whether or not Adam had a navel ." as in sentence"You were not supposed to show your navel on television ."?
Does the word "afforest" mean the same in sentence "After we leave the quarry , we intend to afforest the land and turn it into a nature reserve ." as in sentence"Afforest the mountains ."?
Does the word "solve" mean the same in sentence "Solve an old debt ." as in sentence"Did you solve the problem ?"?
Does the word "purchase" mean the same in sentence "They offer a free hamburger with the purchase of a drink ." as in sentence"They closed the purchase with a handshake ."?
Does the word "software" mean the same in sentence "Did you test the software package to ensure completeness ?" as in sentence"The market for software is expected to expand ."?

```
Ask him a question:
`Does the word "defeat" mean the same in sentence "It was a narrow defeat ." as in sentence"The army 's only defeat ."?
`
You should see the answer "YES".

Now let's try in reverse order:
```
Answer with a single "YES" or "NO"!
Does the word "defeat" mean the same in sentence "The army 's only defeat ." as in sentence"It was a narrow defeat ."?
Does the word "groom" mean the same in sentence "Sheila groomed the horse ." as in sentence"Groom the dogs ."?
Does the word "penetration" mean the same in sentence "Any penetration , however slight , is sufficient to complete the offense ." as in sentence"The penetration of upper management by women ."?
Does the word "hit" mean the same in sentence "An interesting idea hit her ." as in sentence"We hit Detroit at one in the morning but kept driving through the night ."?
Does the word "deliberation" mean the same in sentence "A little deliberation would have deterred them ." as in sentence"He was a man of judicial deliberation ."?
Does the word "navel" mean the same in sentence "You were not supposed to show your navel on television ." as in sentence"They argued whether or not Adam had a navel ."?
Does the word "afforest" mean the same in sentence "Afforest the mountains ." as in sentence"After we leave the quarry , we intend to afforest the land and turn it into a nature reserve ."?
Does the word "solve" mean the same in sentence "Did you solve the problem ?" as in sentence"Solve an old debt ."?
Does the word "purchase" mean the same in sentence "They closed the purchase with a handshake ." as in sentence"They offer a free hamburger with the purchase of a drink ."?
Does the word "software" mean the same in sentence "The market for software is expected to expand ." as in sentence"Did you test the software package to ensure completeness ?"?
```
Ask him a reversed question:
`
Does the word "defeat" mean the same in sentence "The army 's only defeat ." as in sentence"It was a narrow defeat ."?

`

These are the basics of the application. Now you can experiment freely with the model.