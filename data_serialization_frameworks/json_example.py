import json

def serialize_data(data):
    return json.dumps(data)

if __name__ == "__main__":
    data = {"name": "Alice", "age": 30}
    serialized_data = serialize_data(data)
    print(f"Serialized: {serialized_data}")

