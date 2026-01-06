from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

PASTA_BASE = "base"

load_dotenv()

def criar_db():
    #carregar_docs
    #dividir em pedaços(chukns)
    #vetorizar os chunks com processos de embedding
    
    documentos = carregar_documentos()
    chunks = dividir_chunks(documentos)
    # print(len(chunks))
    vetorizar_chunks(chunks)
    print("Chunks criados")
    
def carregar_documentos():
    loaderPDF = PyPDFDirectoryLoader(PASTA_BASE, glob="*.pdf")
    documentos = loaderPDF.load()
    return documentos
    
def dividir_chunks(documentos):
    separador_documentos = RecursiveCharacterTextSplitter(
        chunk_size=1700,
        chunk_overlap=600,                
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""]        
    )
    chunks = separador_documentos.split_documents(documentos)
    return chunks    

def vetorizar_chunks(chunks):
    embedding = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma.from_documents(chunks,
                               embedding, 
                               persist_directory="db"
                               )#Cria o banco vetorizado
    
    
        
criar_db()