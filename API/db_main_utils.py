from django.db import connection

def execute_query(query, params=None, fetch=False):
    with connection.cursor() as cursor:
        cursor.execute(query, params or [])
        if fetch:
            columns = [col[0] for col in cursor.description]
           
            return [dict(zip(columns, row)) for row in cursor.fetchall()]       
        return cursor.rowcount

def fetch_all(query, params=None):
    return execute_query(query, params, fetch=True)

def fetch_one(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params or [])
        row = cursor.fetchone()
        if row:
            columns = [col[0] for col in cursor.description]
            return dict(zip(columns, row))
        return None

def insert(query, params=None):
    return execute_query(query, params)

def update(query, params=None):
    return execute_query(query, params)

def delete(query, params=None):
    return execute_query(query, params)

