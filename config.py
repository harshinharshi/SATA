# config.py
from dotenv import load_dotenv
import sqlite3

def load_environment():
    """Load environment variables from .env file"""
    return load_dotenv()

def get_db_connection(db_path="DB/sata_data_parameter.db"):
    """Get SQLite database connection"""
    return sqlite3.connect(db_path)