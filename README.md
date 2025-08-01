📱 Mobile Review Agent (Agentic AI System)

This project uses open-source LLMs and LangGraph to build a modular Agentic AI pipeline that analyzes mobile phone reviews and classifies feature-level sentiment and ratings (battery, camera, display, etc.).

🚀 Features

🔍 Zero-shot feature-wise sentiment classification using LLMs

🤖 Modular Agentic AI architecture powered by LangGraph

📊 Outputs structured results: sentiment & 0–5 ratings per product feature

🔧 Scalable and easily extendable for summarization, multi-review processing, dashboard UI, etc.

📁 Folder Structure

MobileAgent/├── agents/ # Modular agents (one file per task)│ └── feature_sentiment_agent.py├── langgraph_workflow/ # LangGraph orchestration logic│ └── feature_sentiment_graph.py├── main.py # Entry point script├── requirements.txt # Python dependencies├── .gitignore└── README.md## 🧠 How It Works



1. User provides a mobile product review such as:



   > _"The battery lasts all day, but the camera is disappointing. The display is decent."_



2. The pipeline:

   - Extracts domain-specific features: `battery`, `camera`, `display`, etc.

   - Performs **zero-shot sentiment classification** per feature

   - Maps model confidence to a 0–5 **rating scale**

   - Returns structured sentiment and rating JSON



3. ✅ Sample Output:



```json

{

  "battery": {"sentiment": "positive", "rating": 4.8},

  "camera": {"sentiment": "negative", "rating": 1.5},

  "display": {"sentiment": "neutral", "rating": 2.6}

}