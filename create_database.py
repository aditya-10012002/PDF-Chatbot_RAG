from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

import os
import shutil

CHROMA_PATH = 'chroma'
DATA_PATH = './Data'

def main():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

# def huggingface_embedding():
#     embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
#     return embeddings_model

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="**/*.pdf", show_progress=True)
    docs = loader.load()
    return docs

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True,
    )

    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]):

    if os.path.exists(CHROMA_PATH):
        # shutil.rmtree(CHROMA_PATH)
        os.system('rmdir /S /Q "{}"'.format(CHROMA_PATH))

    # embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}

    embedding_function = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    db = Chroma.from_documents(chunks, embedding_function, persist_directory=CHROMA_PATH)
    # db.persist()

    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == '__main__':
    main()