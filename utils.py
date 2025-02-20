from dotenv import load_dotenv

def load_env_variables():
    return load_dotenv('.env.local') # take environment variables from .env.