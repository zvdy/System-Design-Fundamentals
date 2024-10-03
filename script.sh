#!/bin/bash

# Create main directory
mkdir -p system_design

# Create subdirectories and README.md files
declare -A folders=(
    ["performing_system_design_interview"]="Performing A Systems Design Interview"
    ["database_fundamentals"]="Database Fundamentals"
    ["data_serialization_frameworks"]="Data Serialization Frameworks"
    ["replication"]="Replication"
    ["sharding"]="Sharding"
    ["batch_processing"]="Batch Processing"
    ["stream_processing"]="Stream Processing"
    ["other_types_of_storage"]="Other Types Of Storage"
    ["caching"]="Caching"
    ["load_balancing"]="Load Balancing"
    ["systems_design_interview_patterns"]="Systems Design Interview Patterns"
)

for folder in "${!folders[@]}"; do
    mkdir -p "system_design/$folder"
    echo -e "### ${folders[$folder]}\n\n- **Topic:** ${folders[$folder]}\n- **Summary:** \n" > "system_design/$folder/README.md"
done

# Create example Python files
echo -e "def clarify_requirements():\n    print(\"Understand the problem statement, ask clarifying questions, and gather all necessary requirements.\")\n\nif __name__ == \"__main__\":\n    clarify_requirements()\n" > system_design/performing_system_design_interview/example.py

echo -e "import sqlite3\n\ndef create_table():\n    conn = sqlite3.connect('example.db')\n    c = conn.cursor()\n    c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')\n    conn.commit()\n    conn.close()\n\nif __name__ == \"__main__\":\n    create_table()\n" > system_design/database_fundamentals/relational_databases.py

echo -e "from pymongo import MongoClient\n\ndef create_collection():\n    client = MongoClient('localhost', 27017)\n    db = client['example_db']\n    collection = db['users']\n    return collection\n\nif __name__ == \"__main__\":\n    collection = create_collection()\n" > system_design/database_fundamentals/non_relational_databases.py

echo -e "import json\n\ndef serialize_data(data):\n    return json.dumps(data)\n\nif __name__ == \"__main__\":\n    data = {\"name\": \"Alice\", \"age\": 30}\n    serialized_data = serialize_data(data)\n    print(f\"Serialized: {serialized_data}\")\n" > system_design/data_serialization_frameworks/json_example.py

# Add more example files as needed...

echo "Folder structure and files created successfully."