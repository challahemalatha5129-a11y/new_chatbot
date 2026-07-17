#My chatBot
import streamlit as st
from openai import OpenAI
#page config
st.set_page_config(page_title="Mini ChatGPT - Mistral",page_icon="🤖",layout="centered")
st.title("🤖 Hema Mini ChatGPT - (Mistral AI)")
#==========================================================================================
#API key
api_key="oDyOSs5f4vmdYH23d1CkIMiMg80GsLHF"
#==========================================================================================
#initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages=[{"role":"system","content":"You are helpful AI"}]
#===========================================================================================
for message in st.session_state.messages:
    if message["role"]!="system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
#===========================================================================================
#chat Input
prompt=st.chat_input("Type your Message...")
if prompt:
    if not api_key:
        st.error("Please Enter Mistral API Key.")
        st.stop()
    client=OpenAI(api_key=api_key, base_url="https://api.mistral.ai/v1")
    #display User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
#==============================================================================================
#generate response
    with st.chat_message("assistant"):
       with st.spinner("Thinking..."):
            response=client.chat.completions.create(model="mistral-small-latest",messages=st.session_state.messages)
            reply=response.choices[0].message.content
            st.markdown(reply)
#=========================================================================================================================
    st.session_state.messages.append({"role":"assistant","content":reply})
#================================================================================
#sidebar
with st.sidebar:
    st.header("Options")
    if st.button("Clear Chat"):
        st.session_state.message=[{"role":"system","content":"You are a helpful AI"}]
        st.rerun()
    st.markdown("----")
    st.write("**Model:**Mistral AI")
#===================================================================================================


 





    