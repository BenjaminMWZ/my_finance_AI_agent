from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings

# Create an embedding for each chunk(like a key for a database)
def get_embedding_function():
    # embeddings = BedrockEmbeddings(
    #     client=None,
    #     credentials_profile_name="default", region_name="us-east-1"
    # )
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
