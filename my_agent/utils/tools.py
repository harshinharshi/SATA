# tools.py
import json
import sqlite3
from dotenv import load_dotenv


def load_environment():
    """Load environment variables from .env file"""
    return load_dotenv()


def get_db_connection(db_path="DB/sata_data_parameter.db"):
    """Get SQLite database connection"""
    return sqlite3.connect(db_path)


def fetch_data_required(filter_data, db_path="DB/sata_data_parameter.db"):
    """
    Fetch the 'data required' column value from parameter_table based on dynamic filter criteria.
    
    Args:
        filter_data (dict): Parsed filter criteria as dictionary
        db_path (str): Path to the SQLite database file
        
    Returns:
        dict: JSON formatted result with data required values
    """
    try:
        # Build the WHERE clause dynamically based on available keys
        where_conditions = []
        params = []
        
        # Check for each possible key and add to conditions if present
        if "Module" in filter_data and filter_data["Module"]:
            where_conditions.append("Module = ?")
            params.append(filter_data["Module"])
        
        if "Application" in filter_data and filter_data["Application"]:
            where_conditions.append("Application = ?")
            params.append(filter_data["Application"])
        
        if "Process" in filter_data and filter_data["Process"]:
            where_conditions.append("Process = ?")
            params.append(filter_data["Process"])
        
        # If no conditions are provided, return None
        if not where_conditions:
            print("No valid filter criteria provided")
            return None
        
        # Build the complete SQL query
        where_clause = " AND ".join(where_conditions)
        query = f"SELECT `Data Required` FROM Parameter_table WHERE {where_clause}"
        print(f"Constructed Query: {query}")
        
        # Connect to the database and execute the query
        conn = get_db_connection(db_path)
        cursor = conn.cursor()
        
        print(f"Executing query: {query}")
        print(f"With parameters: {params}")
        
        cursor.execute(query, params)
        result = cursor.fetchone()
        
        conn.close()
        
        # Return the result if found
        if result:
            # Split the result by newlines and remove empty strings
            data_values = [value.strip() for value in result[0].split('\n') if value.strip()]
            
            # Create JSON formatted output
            json_result = {"data required": data_values}
            
            print(f"Final JSON Result: {json.dumps(json_result, ensure_ascii=False)}")
            
            return json_result
        else:
            print("No matching record found")
            return None
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None