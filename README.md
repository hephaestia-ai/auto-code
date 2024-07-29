# Auto Code

Programming CLI bot that digests python files in a specified directory then updates them with refinements


To install:

```zsh
pip install cowgirl-ai-core cowgirl-ai-utils cowgirl-ai-auto-code
```

```zsh 
cowgirl-ai-auto-code refine src .py 
```



This program is currently only compatible with OpenAI, we are looking into expanding compatibility with other open source LLMs such as Meta and Anthropic. We are also investigating adding .sql refinements to the CLI tool.... :) 


New Features
Front end + back end bots

```
front_end refine --file='uicode.js'
back_end refine --file='backendcode.js'

```