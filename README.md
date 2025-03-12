# Setup Guide

## Prerequisites
Ensure that you have a Python virtual environment already set up before proceeding.

## Step 1: Install and Set Up Ollama

1. **Download and Install Ollama**  
   - Visit the official Ollama website: [https://ollama.com/](https://ollama.com/)  
   - Follow the installation instructions for your operating system.

2. **Download Llama 3.1 Model**  
   Run the following command to download Llama 3.1 (8B or lower):
   ```sh
   ollama pull llama3
   ```

3. **Verify LLM Functionality**  
   Check if the language model is working correctly by running:
   ```sh
   ollama run llama3 "Hello, how are you?"
   ```

## Step 2: Install Dependencies
Run the following command to install the required dependencies:
```sh
pip install -r requirements.txt
```

## Step 3: Run the Application
Start the application by executing:
```sh
python app.py
```
or (if using Python 3 explicitly):
```sh
python3 app.py
```

## Troubleshooting
- Ensure that `ollama` is installed and accessible from the terminal.
- Verify that the `llama3` model is downloaded properly.
- Check if all dependencies are installed correctly with `pip list`.

## Additional Resources
For more details, visit [Ollama's official documentation](https://ollama.com/).

