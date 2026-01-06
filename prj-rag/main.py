from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

CAMINHO_DB = "db"

prompt_template = """
Você é um especialista em suporte.
Contexto e informações para dúvidas do cliente:
{base_conhecimento}

Pergunta do cliente: 
{pergunta}

Responda educadamente a pergunta, baseado no contexto acima. 
"""

def perguntar():
    pergunta = input("Faça uma pergunta sobre a empresa: ")

    embedding = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma(
        persist_directory=CAMINHO_DB, 
        embedding_function=embedding
    )

    resultados = db.similarity_search_with_score(pergunta, k=3)#numero de resultados
    
    # print(resultados)
    # return

    if len(resultados) == 0 :
        print("Não foi possível encontrar uma informação")
        return
    
    primeiro_score = resultados[0][1]
    if primeiro_score < 0.7:
        print(f"Não foi possível encontrar informação relevante (score: {primeiro_score:.4f})")
        return
    
    textos = []
    for documento, score in resultados:
        texto = documento.page_content
        textos.append(texto)
        
    base_conhecimento = "\n".join(textos)
    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt.invoke({
        "pergunta": pergunta, 
        "base_conhecimento": base_conhecimento
        })
    
    
    modelo = ChatOpenAI()
    texto_resposta = modelo.invoke(prompt).content
    
    print("\n" + "="*50)
    print("Informações encontradas:")
    print("="*50)
    print(texto_resposta)
    
    
perguntar()