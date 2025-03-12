import pandas as pd

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df, list(df.columns)
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None, None
