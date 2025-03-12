import gradio as gr
import pandas as pd
from csv_handler import load_csv
from query_handler import answer_question
from graph_plotter import generate_plot

df = None
columns = []

def upload_file(file):
    if not file:
        raise gr.Error("Please choose a valid CSV file.", duration=2)
    
    global df, columns
    df, columns = load_csv(file.name)
    if df is not None:
        return f"CSV uploaded successfully! {df.shape[0]} rows and {df.shape[1]} columns.", gr.Dropdown(choices=columns), gr.Dropdown(choices=columns)
    else:
        raise gr.Error("Error loading CSV file. Please check the format.", duration=2)
    
def handle_graph(plot_type, x_column, y_column):
    if df is None:
        raise gr.Error("Please upload a CSV file first.", duration=2)
    return generate_plot(df, plot_type, x_column, y_column)

def handle_query(question):
    if df is None:
        raise gr.Error("Please upload a CSV file first.", duration=2)
    return answer_question(df, question)

with gr.Blocks() as app:
    gr.Markdown("""# xGradio-based CSV Question Answering & Visualization App""")

    gr.Markdown("""# Upload""")
    with gr.Row():
        file_input = gr.File(label="Upload CSV", file_types=[".csv"], interactive=True, scale=2)
        upload_button = gr.Button("Upload", scale=1)
        upload_output = gr.Textbox(label="Upload Status", interactive=True, scale=1)

    gr.Markdown("""# QnA""")
    with gr.Row():
        query_input = gr.Textbox(label="Ask a question about the data")
        query_button = gr.Button("Submit")
        query_output = gr.Textbox(label="Answer", interactive=True)

    gr.Markdown("""# Visualize""")
    with gr.Row():
        plot_type = gr.Dropdown(["Line", "Bar", "Scatter"], label="Plot Type")
        x_column = gr.Dropdown(choices=[], label="X-axis Column")
        y_column = gr.Dropdown(choices=[], label="Y-axis Column")
        graph_button = gr.Button("Generate Graph")
    graph_output = gr.Plot(label="Visualization")

    upload_button.click(upload_file, inputs=[file_input], outputs=[upload_output, x_column, y_column])
    query_button.click(handle_query, inputs=[query_input], outputs=[query_output])
    graph_button.click(handle_graph, inputs=[plot_type, x_column, y_column], outputs=[graph_output])


if __name__ == "__main__":
    app.launch(share=True)