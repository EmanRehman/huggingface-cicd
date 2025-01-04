import gradio as gr
from transformers import pipeline

# Load pre-trained text summarization model from Hugging Face
summarizer = pipeline("summarization")

def summarize_text(text):
    return summarizer(text)[0]['summary_text']

# Define the Gradio interface
iface = gr.Interface(fn=summarize_text, inputs="text", outputs="text", live=True)

# Launch the app
iface.launch()
