# Open AI Playground
Python Project to experiment with Open AI
This project uses Python 3.12.6

## Setup
1. Create a Virtual Environment, run

```powershell
python -m venv venv
```

2. Activate Virtual Environment, run

```powershell
.\venv\Scripts\activate
```

3. Install Dependencies

```powershell
python -m pip install -r .\requirements.txt
```

4. Environment variables
Create a `.env` file in the project root and add the following variables:
- `OPEN_AI_API_KEY` - Your Open AI API Key
- `OPEN_AI_ASST_ID` - Your Open AI Assistant ID


## Virtual Environment

A virtual environment (venv) lets you have a stable, reproducible, and portable environment. You are in control of which packages versions are installed and when they are upgraded.

### Activate Virtual Environment

```ps
.\venv\Scripts\activate
```

### Deactivate Virtual Environment

```ps
deactiavte
```

### Adding a Package

1. Ensure you have activated the virtual Environment
2. Install desired package:

```ps
python -m pip install <package_name>
```

3. Update the `requirements.txt` file with the new package

```ps
python -m pip freeze > requirements.txt
```