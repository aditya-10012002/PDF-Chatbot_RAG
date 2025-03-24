from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_chroma import Chroma
from dotenv import load_dotenv
import argparse
import os

load_dotenv()

CHROMA_PATH = 'chroma'

PROMPT_TEMPLATE = """
Answer the Question based only on the following context:

{context}

---

Answer the Question based on the above context: {question}
"""

def main():

    #Create CLI
    parser = argparse.ArgumentParser(description='Query the PDFs')
    parser.add_argument('query_text', type=str, help='The query text')
    args = parser.parse_args()
    query_text = args.query_text

    #Load the DB
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}

    embedding_function = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    #Search the DB
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    # print(results)
    # print("-----------------------------------------\n\n")
    if len(results) == 0 or results[0][1] < 0.5:
        print(f"Unable to find matching results.")
        return
    
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = PromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash", 
        google_api_key=os.getenv("GOOGLE_API_KEY"), 
        temperature=0
    )
    response_text = model.invoke(prompt)

    sources = {doc.metadata.get("source", None) for doc, _score in results}
    formatted_response = f"Response: {response_text.content}\n\nSources: {sources}"
    print(formatted_response)

if __name__ == '__main__':
    main()