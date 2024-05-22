from langchain_community.llms import Ollama

llm = Ollama(model = "llama2")
result = llm.invoke("Hello, how are you?")
print(result)