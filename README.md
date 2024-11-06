
# AI Content Backend

This is the backend for the AI Content project, built with **Flask**. It generates AI content using OpenAI’s API, stores it in MongoDB Atlas, and serves content history.

## Features

- Generate new AI content on demand
- Store generated content and history in MongoDB
- Serve content history to frontend via REST API

## Technologies

- **Flask** - Python web framework
- **MongoDB Atlas** - Cloud-based NoSQL database
- **OpenAI API** - For AI-generated content
- **Render** - Deployment platform for backend services

## Getting Started

### Prerequisites

- Python 3.8+
- MongoDB Atlas account and database
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/REFATBHUYAN/ai-content-backend
cd ai-content-backend
```
2. Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a .env file for environment variables:

```bash
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/dbname
OPENAI_API_KEY=your_openai_api_key
```

5. Run the Flask app:

```bash
python server.py
```

The server should be running at http://127.0.0.1:5000.

### API Endpoints

POST /generate-content: Generate new AI content
GET /content-history: Retrieve content generation history
