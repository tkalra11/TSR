import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import globalvar
import os
import credentials
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

from nltk.translate.bleu_score import sentence_bleu

from rouge_score import rouge_scorer
scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)

st.set_page_config(page_title="Major 1" , initial_sidebar_state="collapsed" , layout="wide")
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

os.environ['OPENAI_API_KEY'] = credentials.openai_api_key

query = st.text_input('Enter query here:' , 'Query')

submit_button = st.button('Analyse')

if submit_button and  query is not None:
    context_database = Chroma.from_documents(globalvar.inputText, OpenAIEmbeddings())
    embedding_vector = OpenAIEmbeddings().embed_query(query)
    result = context_database.similarity_search_by_vector(embedding_vector)

    similar_results = ''
    for result_page in result:
        seperated = result_page.page_content
        similar_results+=seperated.replace('\n',' ')
        
    prompt_template = """Use the context below to write a response to the query. Use only the information and words provided in the context.
        Context: {similar_results}
        Query: {query}
        Response: """

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["similar_results", "query"]
    )

    llm = OpenAI(temperature=0)

    chain = LLMChain(llm=llm, prompt=PROMPT)

    final_result = chain.apply(input_list=[{'similar_results' : similar_results , 'query' : query}])
    st.write(f'Query : {query}')
    st.write(f'Result : {final_result[0]["text"]}')
    
    rogue_score = scorer.score(similar_results , final_result[0]['text'])
    print(f'Rogue Score : {rogue_score}')
back = st.button('Back')
if back:
        globalvar.inputText = ''
        switch_page('main_page')