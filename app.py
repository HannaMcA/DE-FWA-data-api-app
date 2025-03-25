# app.py
from flask import Flask, request, jsonify
import pandas as pd
import ssl

app = Flask(__name__)
ssl._create_default_https_context = ssl._create_unverified_context

@app.route('/data', methods=['POST'])
def process_data():
    try:
        base_url = "https://data.cityofnewyork.us/resource/uvpi-gqnh.csv"
        # limit = 50000
        limit = 5000
        offset = 0
        all_chunks = []

        # while True:
        #     url = f"{base_url}?$limit={limit}&$offset={offset}"
        #     print(f"Fetching rows {offset} to {offset + limit}...")
        #     chunk = pd.read_csv(url)
        #     if chunk.empty:
        #         break
        #     all_chunks.append(chunk)
        #     offset += limit

        #df = pd.concat(all_chunks, ignore_index=True)

        #lets just get 5k rows for the api
        df = pd.read_csv(f"{base_url}?$limit={limit}")
        print(f"Retrieved {len(df)} rows.")

        return jsonify({"message": "CSV processed successfully", "rows": len(df)})
    except Exception as e:
        return jsonify({"message": "Failed to process CSV", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
