from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader

class UerrBot:
    def __init__(self, api_key, model="llama-3.3-70b-versatile"):
        self.api_key = api_key
        os.environ['GROQ_API_KEY'] = self.api_key
        self.chat = ChatGroq(model=model)

    def carregar_documentos(self, url):
        loader = WebBaseLoader(url)
        return loader.load()

    def concatenar_conteudo(self, lista_documentos):
        documento = ""
        for doc in lista_documentos:
            documento += doc.page_content
        return documento

    def construir_chain(self):
        template = ChatPromptTemplate.from_messages([
            {"role": "system", "content": "Você é um assistente chamado Asimov e acessa informações fornecidas para responder perguntas."},
            {"role": "user", "content": "Com base nas informações extraídas do site, responda a pergunta\n\n {pergunta}\n\n{documentos_informados}"}
        ])
        return template | self.chat

    def perguntar(self, documentos_informados, pergunta):
        chain = self.construir_chain()
        resposta = chain.invoke({
            "documentos_informados": documentos_informados,
            "pergunta": pergunta,
            "input": pergunta
        })
        return resposta.content



def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")  # pega a chave do .env
    url = "https://uerr.edu.br"
    pergunta = input(f' Qual a pergunta para o portal {url} : ')

    bot = UerrBot(api_key)
    documentos = bot.carregar_documentos(url)
    conteudo = bot.concatenar_conteudo(documentos)
    resposta = bot.perguntar(conteudo, pergunta)

    print("🤖 UerrChat:", resposta)


if __name__ == "__main__":
    main()