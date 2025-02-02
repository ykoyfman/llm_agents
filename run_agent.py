from llm_agents import Agent, ChatLLM, PythonREPLTool, HackerNewsSearchTool, SerpAPITool, PipInstallTool

if __name__ == '__main__':
    prompt = input("Enter a question / task for the agent: ")
    agent = Agent(llm=ChatLLM(), tools=[PythonREPLTool(), SerpAPITool(), HackerNewsSearchTool(), PipInstallTool()])
#    agent = Agent(llm=ChatLLM(), tools=[PythonREPLTool()])
    result = agent.run(prompt)

    print(f"Final answer is {result}")
