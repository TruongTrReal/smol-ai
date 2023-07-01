```python
import json
from pymongo import MongoClient

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_data(data):
    extracted_data = []
    for item in data:
        extracted_item = {
            "Code": item["Code"],
            "Name": item["Name"],
            "TotalShares": item["TotalShares"],
            "URL": item["URL"],
            "Exchange": item["Exchange"],
            "IndustryName": item["IndustryName"]
        }
        extracted_data.append(extracted_item)
    return extracted_data

def send_to_mongodb(data, connection_string, db_name, collection_name):
    client = MongoClient(connection_string)
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(data)

def main():
    file_path = 'data.json'  # replace with your json file path
    connection_string = ''  # replace with your MongoDB Atlas connection string
    db_name = ''  # replace with your database name
    collection_name = ''  # replace with your collection name

    data = read_json_file(file_path)
    extracted_data = extract_data(data)
    send_to_mongodb(extracted_data, connection_string, db_name, collection_name)

if __name__ == "__main__":
    main()
```