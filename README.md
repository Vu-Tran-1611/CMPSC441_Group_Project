## Requirements 

- Conda installed (Miniconda or Anaconda, Link: https://www.anaconda.com/download) for python packages manage (You can use other if you wish, but below is tutorial for Conda)
- Visual Sudio Code 


## 1. GET THE PROJECT

Clone or download the repository as a ZIP, extract it, and open the extracted project folder in VS Code. The project folder should contain `environment.yml` and `.env.example`. 
Remove .example in .env.example 

## 2. CREATE CONDA ENVIRONMENT
Now you should be inside the project, open the terminal inside VSCode and run below commands. Note: You will see the word "base" in the first word of the first line in terminal

```bash
conda env create -f environment.yml
```
This command do 2 things: 
1. creating environment in Conda system, this enviroment will store all the necessary packages that used for this repo only
2. Download all the packages from environment.yml into that environment


```bash
conda activate cmpsc-441-group-project
```
You need to activate the envrionment that you just created to run all the files (i.e: layer_0,layer_1,....). Note: After activate, You should see the phrase "cmpsc-441-group-project" instead "base" in the first line in terminal that means the environment that you just created is actually activated.


## 3. SET UP FOR LOCAL MODEL (SKIP IF YOU USE ClOUD MODEL): Install and prepare Ollama 

As mentioned there are 2 ways to achieve LLM: 
1. Cloud Model - no need to download, hosting, super intelligent model, super fast running but pay moneys for number of tokens used (words that you send to LLM)

2. Local Model - need to DOWNLOAD and HOST model, but don't have to spend any money  

Ollama is a software that help you to DOWNLOAD, manage and HOST model (LLM).  


1. Visit [ollama.com/download](https://ollama.com/download) and download 
2. Open the Ollama app and leave it running while using Ollama-based scripts.
3. Go back to Terminal that you openned with environment active (activated), download the models by the scripts below 
4. I tested 2 local models: qwen3:1.7b (1.7 billion Parameters - 1.4GB), The correctness is prettly low (< 40%), qwen3:8b (8 billion Parameters - 5.2 GB), the correctness is around 60% - 80%, you may select any models you like on Ollama website, but read the description to see whether model be ABLE TO CALL TOOLS, if model cannot call tools, you cannot use to build agent! 


   ```bash
   ollama pull qwen3:8b
   ```


5. Confirm the models are available:

   ```bash
   ollama list
   ```

If the `ollama` command is not found, finish installing the Ollama app, open it, and restart Terminal.



## 4. SET UP FOR CLOUD MODEL (SKIP IP YOU USE LOCAL MODEL):  
For the sake of clarity, I decided that you will not give me any money for cloud model, instead you will sign up an account with your favourite provider and obtain their api key, then pay credits by yourself. 
1. Choose any cloud model providers you prefer (OpenAI, Google, Anthropic....) - I have been using OpenAI 
2. If you like OpenAI go to https://platform.openai.com/
3. Create an account and then click on "API keys" on left sidebar, then create secret key
4. They should ask you to save the key, you just need to copy that and paste into .env file  
next to OPENAI_API_KEY. (i.e: OPENAI_API_KEY = sk_sadasd123123_asdasfqewe_dasd123123_asdasdscx) 
5. The other providers are similar. 

## 5. SET UP FOR LANGSMITH: 
Langsmith is a website that allow you to keep track of number of tokens, money cost, time response, agent internal thoughts for each conversation and so many other helpful features. 
When you put the decorator @tool on the top of function, Langsmith will automatically keep track of this tool and other things. 

1. Go to https://smith.langchain.com/ 
2. Create an account
3. Click on "tracing" on left side bar, select connect agent and name your agent 
4. Click on generate api key, in the box configuration environment, switch to tab .env, copy everything
and paste into .env below LangSmith. 
5. Now whenever you talk with agent, you will see everything is traced in "tracing"
