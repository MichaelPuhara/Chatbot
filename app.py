import os
import openai
import streamlit as st
#import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
#openai.api_key = "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"

api_key = os.environ["OPENAI_API_KEY"]

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = " "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



st.title("Pātai Bot Aotearoa")

history = st.empty()

message = st.text_input(prompt)

if message:
    history, output = chatgpt_clone(message, history)
    st.write(start_sequence + output)

