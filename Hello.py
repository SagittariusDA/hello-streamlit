import streamlit as st
from langchain.llms import OpenAI

st.title('Quikstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')
#st.sidebar.text_area('爱发电页面', 'https://afdian.net/a/Kaptech')
st.sidebar.text_area('Man Wang', 'github.com/SagittariusDA')
def generate_response(input_text):
	llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
	st.info(llm(input_text))

with st.form('my_form'):
	text = st.text_area('Enter text:', 'What?')
	submitted = st.form_submit_button('Submit')
	if not openai_api_key.startswith('sk-'):
		st.warning('Wrong key')
	if submitted and openai_api_key.startswith('sk-'):
		generate_response(text)
