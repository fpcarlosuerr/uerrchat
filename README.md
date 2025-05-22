# 🎓 Apresentação do Projeto: UerrBot

---

## 🎯 Slide 1 – Abertura

Olá a todos!  
Hoje vou apresentar o **UerrBot**, um assistente virtual que responde perguntas com base nas informações disponíveis no portal da **Universidade Estadual de Roraima (UERR)**.

---

## 🧠 Slide 2 – Motivação

- A UERR possui um portal com muitas informações distribuídas em diversas páginas.
- Navegar por esse conteúdo pode ser difícil e demorado.
- O UerrBot automatiza esse processo com uso de IA e web scraping.

---

## ⚙️ Slide 3 – Tecnologias Utilizadas

- **Python**
- `requests` + `BeautifulSoup` – Web scraping
- `langchain` + `ChatGroq` – Modelo LLM (LLaMA3)
- `WebBaseLoader` – Carregamento de conteúdo web
- `SequenceMatcher` – Cálculo de similaridade textual

---

## 🏗️ Slide 4 – Estrutura do Código

Classe `UerrBot` com os principais métodos:

- `extrair_links_internos(url_base)`
- `filtrar_links_por_contexto(links, pergunta)`
- `carregar_documentos(url_base, pergunta)`
- `concatenar_conteudo(lista_documentos)`
- `construir_chain()`
- `perguntar(documentos_informados, pergunta)`

---

## 🔍 Slide 5 – Fluxo de Execução

1. Usuário faz uma pergunta
2. O bot coleta e filtra links do portal
3. Carrega o conteúdo das páginas relevantes
4. Concatena o conteúdo
5. Envia ao modelo LLaMA3 para obter a resposta

---

## 🧪 Slide 6 – Demonstração (opcional)

**Exemplo de pergunta:**

> “Quais são os cursos oferecidos pela UERR?”

O bot:

- Acessa o site da UERR
- Lê os textos das páginas relevantes
- Gera uma resposta baseada nesses conteúdos

---

## ⚠️ Slide 7 – Cuidados e Melhorias

- Requer **chave de API válida** (ChatGroq)
- Tratamento de erros para links inválidos ou lentos
- Pode ser melhorado com:
  - Cache de páginas
  - Interface gráfica
  - Tradução ou suporte a linguagem natural mais flexível

---

## 🚀 Slide 8 – Conclusão

O **UerrBot** é um exemplo de aplicação prática de IA:

- Facilita o acesso a informações públicas
- Automatiza leitura, interpretação e resposta
- Reduz o tempo de busca por informações relevantes

---

## ❓ Slide 9 – Perguntas

Agora abro espaço para perguntas e sugestões.  
Muito obrigado!

---
