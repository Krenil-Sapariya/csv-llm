import ollama
import pandas as pd
from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str
    data_summary: str
    numerical_analysis: str

def summarize_dataframe(df):
    summary = f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns."
    summary += f" Column names: {', '.join(df.columns)}."
    return summary

def analyze_numerical_data(df):
    numerical_cols = df.select_dtypes(include=["number"])
    if numerical_cols.empty:
        return "No numerical columns found in the dataset."
    stats = numerical_cols.describe().to_string()
    return f"Numerical column analysis:\n{stats}"

def answer_question(df, question):
    if df is None:
        return "No data available. Please upload a CSV file first."
    
    if question.strip()=="":
        return "Please ask your question !!"
    
    data_summary = summarize_dataframe(df)
    numerical_analysis = analyze_numerical_data(df)
    query = QueryRequest(question=question, data_summary=data_summary, numerical_analysis=numerical_analysis)
    
    prompt = f"""
    the full csv is: {df}
    User Question: {query.question}
    Provide a helpful and concise response to the user question.
    """
    
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    
    return response.get("message", "No response from LLM").get("content")
