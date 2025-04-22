
# VidSearch

VidSearch is a web application that allows you to perform smart searches within a video database using semantic similarity powered by OpenAI embeddings.

## 🌐 Overview

- **Frontend**: HTML/CSS/JavaScript providing a clean search interface and video card results.
- **Backend**: Python Flask server handling search requests and returning the most relevant videos based on text similarity.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API Key (using `text-embedding-ada-002` model)
- `pip` installed
- A simple HTTP server to serve `index.html` (optional)

### Installation

1. Clone this repository:

```bash
git clone <your-repo-url>
cd vidsearch
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key
```

4. Place your `dataset.json` file inside a `data/` folder.

### Start the Backend Server

```bash
python server.py
```

The server will run at `http://127.0.0.1:5000`.

### Launch the Frontend

Simply open `index.html` in your browser, or use a local server:

```bash
python -m http.server
```

Then navigate to `http://localhost:8000`.

## 📂 Project Structure

```
├── data/
│   └── dataset.json       # Video data and embeddings
├── server.py              # Flask backend server
├── utils.py               # Utility functions (embedding & similarity)
├── index.html             # Static frontend
├── .env                   # Environment variables (OpenAI key)
```

## 🧠 Features

- Semantic search using OpenAI embeddings
- Similarity filtering (threshold set to 0.75)
- Responsive UI with loading indicators and error handling
- Option to select number of search results

## 📦 Dependencies

- Flask
- Flask-CORS
- python-dotenv
- openai
- pandas
- numpy

Install them via:

```bash
pip install flask flask-cors python-dotenv openai pandas numpy
```

## 📜 License

This project is licensed under the MIT License.
