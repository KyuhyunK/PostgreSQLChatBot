import requests
import json
from config import RAPIDAPI_KEY


def validate_sql_columns(sql_query, valid_columns):
    sql_keywords = {'SELECT', 'AS', 'FROM', 'WHERE', 'GROUP', 'BY', 'ORDER', 'DESC', 'LIMIT', 'SUM', 'AVG', 'COUNT'}
    sql_query_columns = [word.strip('`,') for word in sql_query.split() if word.strip('`,').isalpha() and word.upper() not in sql_keywords]
    invalid_columns = [col for col in sql_query_columns if col.lower() not in [col.lower() for col in valid_columns]]
    corrected_query = sql_query
    for invalid_col in invalid_columns:
        if invalid_col == 'revenue':
            corrected_query = corrected_query.replace('revenue', 'total_revenue')
        # Add more replacements if necessary
    return corrected_query


def invoke_amazon_api(endpoint, params):
    url = f"https://ai-query2.p.rapidapi.com/{endpoint}"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "ai-query2.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=params)
    data = response.json()
    return data

def invoke_amazon_response(prompt):
    endpoint = "optimize_sql_query"
    params = {"prompt": prompt, "model": "oa_v3_16k", "data_source_type": "postgresql"}
    data = invoke_amazon_api(endpoint, params)
    return data



def invoke_chain(user_question, valid_columns):
    # Prepare the prompt for generating the SQL query
    sql_query_prompt = f"Generate a SQL query for the following question: {user_question}. The default table name is 'aggregate_profit_data', unless specified otherwise use this table name. Ensure the query includes the table name and the 'FROM' keyword. Use only valid columns from the following list: {', '.join(valid_columns)}. Keep your response concise and easy to understand."
    
    # Use the Amazon API to generate the SQL query
    params = {
        "prompt": sql_query_prompt,
        "model": "oa_v3_16k",
        "data_source_type": "postgresql"
    }
    response = invoke_amazon_api("generate_sql", params)
    
    generated_sql_query = response.get('result', '')

    print("Generated SQL Query:", generated_sql_query)

    # Validate and correct the SQL query if needed
    corrected_sql_query = validate_sql_columns(generated_sql_query, valid_columns)

    return corrected_sql_query


