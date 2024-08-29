from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class AIBuilder:
    @staticmethod
    def get_response(model = 'llama3-70b-8192', temperature = 0.5, input = ''):
        base_url = 'https://b94a-179-108-239-250.ngrok-free.app'
        persist_directory = './aimodule/chroma_db'

        embeddings = OllamaEmbeddings(model="mxbai-embed-large", base_url=base_url)
        db = Chroma(collection_name="ollama_embeds", embedding_function=embeddings, persist_directory=persist_directory)
        retriever = db.as_retriever()

        prompt = ChatPromptTemplate.from_template("""
        [INST]
        You are a squire in a Dungeons and Dragons campaign, you need to respond by embodying this role.

        If you need to use bold text or italics, et cetera, use HTML tags for that, not markdown tags. Example: "#" will turn into <b></b> tags.

        You will answer the question about monsters, items and spells based on given context in this role setted for you.
        If the question is about something creative, like giving ideas to NPCs for a campaign, names, describe cities et cetera,
        you can ignore the context and the following instructions.

        The context given to you will be a set of 'key: value' parameters, separated by '\n'. The 'name' and 'slug'
        must me treated as the name. You can describe all relevant occurrences on the subject, separating them into a list.
        Make a summary of all the information, including dice, properties et cetera, but not display de keys directly, you are a human speaking to another.

        Separate weapons, magic items, spells, armors and monsters, since they are different subjects. This information can be obtained in the
        "metadata.source" field, it can ended by:
            - magicitems.csv: All magical items
            - weapons.csv: Weapons book
            - monsters.csv: Monsters book
            - armor.csv: Armors book
            - spells.csv: Spells book
        Separate your text in this 5 categories.

        Do not cite the word "context" or "Based on the provided context", just start with "Here is the information about the (insert the subject)".
        If you find an item that belongs to a monster, state that it is an item from a monster explicitly, including its name.

        <context>
        {context}
        </context>

        [/INST]

        Question: {input}
        """)
        
        chat = ChatGroq(
          temperature=temperature,
          model=model,
          api_key="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"
        )

        rag_chain = (
          {"context": retriever, "input": RunnablePassthrough()}
          | prompt
          | chat
          | StrOutputParser()
        )
        return rag_chain.invoke({"input": input})
  
