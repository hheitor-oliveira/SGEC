# lib's import's
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
  '''Essa classe é responsável por realizar a conexão com o banco de dados para realizar as comunicações.'''
  @staticmethod
  def get_connection() -> psycopg.Connection:
    
    try:
      connection = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
      )
      return connection
    
    except psycopg.Error:
      raise psycopg.Error()