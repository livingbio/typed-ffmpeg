- the originoal idea is start after GPT-3 is released, but I don't have time to work on it.
- The ffmpeg document is not easy to read, so I want to make a simple document for it.
- At beginning, I want to do an End to End genrator, given ffmpeg document than generate python code,
- However since there are too many filters need to be implemented, and always have some little glitch I decide to do it step by step.
- I did some POC about use ChatGPT to generate Python code, it works
- Some bug include generate not complete JSON code
- The docstring format is not consistence each time I used it.
- most of the filters I never used,


Future Work
- generate python code from ffmpeg code instead of document, maybe it is easier to do it.
- findout some way to test the genereate code, so the GPT can learn from the test result and generate better code. improve itself
