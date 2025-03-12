import matplotlib.pyplot as plt
import seaborn as sns
import gradio as gr

def generate_plot(df, plot_type, x_col, y_col):
    if x_col not in df.columns or y_col not in df.columns:
        raise gr.Error("Please select valid columns!")

    if not plot_type:
        raise gr.Error("Select Plot type first!")

    fig, ax = plt.subplots(figsize=(8, 5))

    if plot_type.lower().strip() == "scatter":
        sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
    elif plot_type.lower().strip() == "line":
        sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
    elif plot_type.lower().strip() == "bar":
        sns.barplot(data=df, x=x_col, y=y_col, ax=ax)
    else:
        return None

    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f"{plot_type.capitalize()} Plot of {y_col} vs {x_col}")

    return fig
