import requests, pandas

conn = pandas.DataFrame(requests.get("http://127.0.0.1:8000/items_processed").json())

print(conn.head())