# Agentic E-Commerce: An Intelligent Shopping System With Multi-Agent Orchestration


## 0. REQUIREMENTS:

- Conda installed (Miniconda or Anaconda, Link: https://www.anaconda.com/download) for python packages manage (You can use other if you wish, but below is tutorial for Conda)
- Visual Sudio Code 

## 1. GET THE PROJECT:

Clone or download the repository as a ZIP, extract it, and open the extracted project folder in VS Code. The project folder should contain `environment.yml` and `.env.example`

## 2. CREATE CONDA ENVIRONMENT:
Now you should be inside the project, open the terminal inside VSCode and run below commands. Note: You will see the word "base" in the first word of the first line in terminal

```bash
conda env create -f environment.yml
```
This command do 2 things: 
1. Create an environment in Conda system, this enviroment will store all the necessary packages that used for this repos only
2. Download all the packages from environment.yml into that environment


```bash
conda activate cmpsc-441-group-project
```
You need to activate the environment that you just created to run all the files (i.e: layer_0,your agent file,....). Note: After activate, You should see the phrase "cmpsc-441-group-project" instead "base" in the first line in terminal, that means the environment that you just created is actually activated.


## 3. ACHIEVE MODEL: 
As mentioned there are 3 ways to achieve LLM: 

### Cloud Model:
- No need to download the model
- No need to host the model
- Achieve super intelligent LLM 
- Achieve super fast response time from LLM

=> But pay moneys for number of tokens used (words that you send to LLM)

### Local Model on your computer
- Need to DOWNLOAD the model 
- Need to HOST the model
 
=> But don't have to spend any money  

### Local Model On SunLab 
- Need to DOWNLOAD the model on SunLab computer 
- Need to HOST the model on SunLab computer
- Open and maintain ssh tunnel so your computer can communicate with Sun Lab computer  

## 4. SET UP FOR LOCAL MODEL ON YOUR COMPUTER (SKIP IF YOU USE CLOUD MODEL):

### Ollama is a software that help you to DOWNLOAD, manage and HOST model (LLM).  

1. Visit [ollama.com/download](https://ollama.com/download) and download the software
2. Open the Ollama app and leave it running
3. Go back to Terminal that you openned with environment activated, download the models by the scripts below (read step 4 before you run the scripts)

   ```bash
   ollama pull qwen3:8b
   ```

4. I tested 2 local models:  

   Correctness is the accuracy of the agent's response and user/developer expectations. It is NOT the accuracy of the information in the agent's response, because this information is outside the knowledge of the AGENT (i.e., from a database, the Internet, etc.).
   
   For example, regarding correctness: I (developer) want the response from the agent to be line by line, but it puts everything on a single line

   ### qwen3:1.7b 
   - Parameters: 1.7 billion 
   - Storage: 1.4GB 
   - Response time: ~ 30s 
   - The correctness: ~40% (likely to make up the answer - HALLUCINATION )
   ### qwen3:8b 
   - Parameters: 8 billion 
   - Storage: 5.2 GB 
   - Response time: ~ 35s
   - The correctness: 60% - 70% (likely to make up the answer - HALLUCINATION )

You may select any models you like on Ollama website, but read the description to see whether model be ABLE TO CALL TOOLS (with tools tag), if model cannot call tools, you cannot use to build agent!
You may need to consider these criteria when selecting local model: 
   - Be able to understand user query 
   - Be able to call the tool
   - Be able to call the RIGHT tools based on user query
   - Be able to extract the CORRECT parameters from user query 
   - Be able to pass those parameters into tools  
   
Model qwen3:8b can do pretty well of all above criteria, but again choice is yours



5. Confirm the models are available:


   ```bash
   ollama list
   ```

If the `ollama` command is not found, finish installing the Ollama app, open it, and restart Terminal.



## 5. SET UP FOR CLOUD MODEL (SKIP IF YOU USE LOCAL MODEL):  
For the sake of clarity, I decided that you will not give me any money for cloud model, instead you will sign up an account with your favourite provider and obtain their api key, then pay credits by yourself. 
1. Choose any cloud model providers you prefer (OpenAI, Google, Anthropic....) - I have been using OpenAI 
2. If you like OpenAI go to https://platform.openai.com/
3. Create an account and then click on "API keys" on left sidebar, then create secret key
4. They should ask you to save the key, you just need to copy that and paste into .env file  
next to OPENAI_API_KEY. (i.e: OPENAI_API_KEY = sk_sadasd123123_asdasfqewe_dasd123123_asdasdscx) 
5. The other providers are similar.  
6. I tested 2 cloud GPT models: 
   ### GPT 5.5 
   - Parameters: 7~10 Trillion 
   - Response Time: ~ 8s-9s 
   - Cost: ~ $0.03-$0.05
   - The correctness: ~ 99%-100%. 
   ### GPT 5.4-mini 
   - Parameters: Between 1T and 7T 
   - Response Time: ~ 4s-5s 
   - Cost: ~ $0.004-$0.01
   - The correctness: ~ 96% - 100%



## 6. SET UP FOR LANGSMITH: 
Langsmith is a website that allow you to keep track of number of tokens, money cost, time response, agent internal thoughts for each conversation and so many other helpful features. 
When you put the decorator @tool on the top of function, Langsmith will automatically keep track of this tool and other things. 

1. Go to https://smith.langchain.com/ 
2. Create an account
3. Click on "tracing" on left side bar, select connect agent and name your agent 
4. Click on generate api key, in the box configuration environment, switch to tab .env, copy everything
and paste into .env below LangSmith. 
5. Now whenever you talk with agent, you will see everything is traced in "tracing"


## 7. READ NECESSARY FILES: 
1. layer_0.py: basic things about Langchain 
2. shopping_agent.py, product_tools.py: How I implemented agent for the current website 
3. Other files are optional if you are interested in Agentic RAG (or your tools need RAG) and LangChain ecosystem 

## 8. START BUILDING AGENT AND TOOL: 
1. Each of us should come up with two tools and one agent to test whether your agent can choose the right tool and pass the correct parameters. Ideally, both tools should handle related tasks - for example, two user-related tools or two product-related tools. 
2. Let me know what specific tool you will build, including input, output and detail descrition of the tool so I can provide you website api. 

