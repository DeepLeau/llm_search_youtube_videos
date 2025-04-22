from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
import pandas as pd

from utils import get_videos

load_dotenv()

app = Flask(__name__)
CORS(app)

SIMILARITIES_RESULTS_THRESHOLD = 0.75

DATASET_PATH = "data/dataset.json"
df = pd.read_json(DATASET_PATH).drop(columns=["text"], errors="ignore").fillna("")

@app.route('/search', methods=['POST'])
def search_videos():
    data = request.get_json()
    query = data.get("query", "")
    number_of_rows = data.get("number_of_rows", 10)

    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    videos = get_videos(df, query, number_of_rows)

    result = videos.drop(columns=["ada_v2"]).to_dict(orient="records")

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)