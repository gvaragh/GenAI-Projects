from langchain_ollama import OllamaEmbeddings


embed = OllamaEmbeddings(model="llama2:7b")
embedding = embed.embed_query("Hello Ollama!")
print(embedding)
