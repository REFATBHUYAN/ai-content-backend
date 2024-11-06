from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from pymongo import MongoClient
from dotenv import load_dotenv
import datetime
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

app.run(host='0.0.0.0', port=5000, debug=True)


# Set up MongoDB Atlas connection
try:
    client = MongoClient(os.getenv("MONGODB_URI"))
    db = client['ai_content_db']  # Use 'ai_content_db' database
    client.admin.command('ping')  # Test connection
    print("MongoDB Atlas connection successful!")
except Exception as e:
    print(f"Failed to connect to MongoDB Atlas: {e}")

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/generate-content', methods=['POST'])
def generate_content():
    try:
        # Generate AI content using the latest `gpt-3.5-turbo` model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Provide some insightful content"}],
            max_tokens=50
        )
        content = response['choices'][0]['message']['content'].strip()

        # Store generated content in MongoDB
        db.content.insert_one({
            "content": content,
            "timestamp": datetime.datetime.utcnow()
        })
        return jsonify(content=content), 200

    except Exception as e:
        # Print the error to the terminal for debugging
        print("Error in /generate-content:", e)
        return jsonify(error=str(e)), 500


@app.route('/content-history', methods=['GET'])
def content_history():
    try:
        # Retrieve content history from MongoDB
        history = list(db.content.find({}, {"_id": 0}))
        return jsonify(history=history), 200
    except Exception as e:
        print("Error in /content-history:", e)
        return jsonify(error=str(e)), 500


# Run the server in debug mode
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
