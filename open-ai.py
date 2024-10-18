import openai
from dotenv import load_dotenv
import os

load_dotenv()

def ler_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        return file.read()
    

def resumo(texto):
    

