import pandas as pd
import gradio as gr
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from pandasai import SmartDataframe
from pandasai import SmartDatalake
import warnings
warnings.filterwarnings(action = 'ignore')
# from pandasai import PandasAI

# Set the PANDASAI_API_KEY environment variable
import os
os.environ['PANDASAI_API_KEY'] = "Your PandasAI key"

def analyze_data(file, prompt):
    # Load the data
    df = pd.read_csv(file.name)   # for xlsx file change it to pd.read_excel
    # Create a SmartDataframe
    sdf = SmartDataframe(df)
    # Perform chat-based analysis
    response = sdf.chat(prompt)

    # Check if the response contains a plot-related keyword
    if "plot" in response.lower():
        # Generate a sample plot
        plt.figure(figsize=(8, 6))
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # Sample data for plotting
        plt.title("Sample Plot")
        # Save the plot as a temporary file
        plot_filename = "sample_plot.png"
        plt.savefig(plot_filename)
        plt.close()
        # Return the plot filename
        return plot_filename
    else:
        return response

# Create a file uploader interface
file_uploader = gr.File(label="Upload CSV File")

# Create a text input for user prompt
text_input = gr.Textbox(label="Enter your prompt")

# Create a Gradio interface
gr.Interface(analyze_data, inputs=[file_uploader, text_input], outputs="text").launch()
