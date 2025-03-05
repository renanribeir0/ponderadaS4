from supabase import create_client, Client
from config.settings import SUPABASE_URL, SUPABASE_API_KEY


supabase: Client = create_client(SUPABASE_URL, SUPABASE_API_KEY)

def consultar_todos_logs():


    all_data = []
    batch_size = 1000 
    start = 0

    while True:

        response = supabase.table("logs").select("*").range(start, start + batch_size - 1).execute()

        if response.data:
            all_data.extend(response.data)
            start += batch_size  
        else:
            break  

    return all_data
