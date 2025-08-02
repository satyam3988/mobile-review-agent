📱 Mobile Review Agent (Agentic AI System)

This project uses open-source LLMs and LangGraph to build a modular Agentic AI pipeline that analyzes mobile phone reviews and classifies feature-level sentiment and ratings (battery, camera, display, etc.).

🚀 Features

🔍 Zero-shot feature-wise sentiment classification using LLMs

🤖 Modular Agentic AI architecture powered by LangGraph

📊 Outputs structured results: sentiment & 0–5 ratings per product feature

🔧 Scalable and easily extendable for summarization, multi-review processing, dashboard UI, etc.

🌐 **Dual Interface**: Command-line and web interfaces for different use cases

## 🚀 Quick Start

### **Command Line Interface**
```bash
python main.py
```

### **Web Interface (Streamlit)**
```bash
streamlit run streamlit_app.py
```

## 🌐 Access the Web App

Once running with `streamlit run streamlit_app.py`, the app will be available at:
- **Local**: http://localhost:8501
- **Network**: http://your-ip:8501

## 📁 Folder Structure

MobileAgent/├── agents/ # Modular agents (one file per task)│ └── feature_sentiment_agent.py├── langgraph_workflow/ # LangGraph orchestration logic│ └── feature_sentiment_graph.py├── main.py # CLI entry point script├── streamlit_app.py # Web interface├── requirements.txt # Python dependencies├── .gitignore└── README.md

## 🧠 How It Works

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
```

## 🎯 Interface Options

### **CLI Mode (`main.py`)**
- Traditional command-line interface
- Step-by-step phone selection
- Text-based output
- Perfect for automation and scripting
- Fast execution for quick analysis

### **Web Mode (`streamlit_app.py`)**
- Modern web interface
- Interactive dropdown selection
- Visual charts and metrics
- Responsive design for all devices
- Real-time processing with progress indicators
- Beautiful UI with custom styling

## 🔧 Dependencies

All dependencies are included in `requirements.txt`:

```txt
# Core dependencies
transformers==4.54.1
langgraph==0.6.2
pandas==2.3.1

# Web interface
streamlit==1.47.1
```

## 📋 Usage Examples

### **CLI Usage**
```bash
# Run CLI interface
python main.py

# Output will be:
# 📱 Available Phones:
# 1. iPhone 14 Pro
# 2. Samsung Galaxy S23
# ...
# 🔢 Enter the number of the phone to summarize: 1
```

### **Web Usage**
```bash
# Run web interface
streamlit run streamlit_app.py

# Opens browser at http://localhost:8501
```

## 🚀 Running in Production

For production deployment:

```bash
# Set environment variables
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Run with production settings
streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
```

## 🎨 Web Interface Features

### **Interactive Phone Selection**
- Dropdown menu with all available phones
- Real-time data loading with progress indicators
- Smart search and filtering capabilities

### **Analytics Dashboard**
- **Quick Stats**: Average rating, positive/negative feature counts
- **Bar Charts**: Visual breakdown of feature ratings
- **Review Count**: Number of reviews analyzed

### **Feature-wise Analysis**
- **Sentiment Analysis**: Positive/Negative sentiment for each feature
- **Rating Scores**: 1-5 star ratings for each feature
- **Visual Cards**: Clean, modern UI for feature display

### **Comprehensive Summary**
- AI-generated summary of all reviews
- Highlighted key insights and trends
- Professional formatting with custom styling

## 🔍 Troubleshooting

### Common Issues:

1. **Port already in use**: Change the port in the command
   ```bash
   streamlit run streamlit_app.py --server.port 8502
   ```

2. **Data loading issues**: Check if the data files are in the correct location

3. **Memory issues**: The app loads all phone data at startup, ensure sufficient RAM

## 🎨 Customization

You can customize the app by modifying:
- **CLI**: Edit `main.py` for command-line behavior
- **Web**: Edit `streamlit_app.py` for web interface
- **Styling**: Modify CSS in the Streamlit app
- **Layout**: Adjust columns and sections as needed

## 📊 Performance Tips

1. **CLI**: Faster for quick analysis and automation
2. **Web**: Better for exploration and visualization
3. **Caching**: The web app uses Streamlit's built-in caching
4. **Efficient Processing**: Reviews are processed in batches

## 🔗 Integration

The application integrates seamlessly with your existing:
- `data_loader` modules
- `langgraph_workflow` components
- `agents` for sentiment analysis

## 📱 File Structure

```
mobile-review-agent/
├── main.py              # CLI interface
├── streamlit_app.py     # Web interface
├── agents/              # AI agents
├── langgraph_workflow/  # Workflow orchestration
├── data_loader/         # Data loading utilities
└── requirements.txt     # Dependencies
```

---

**Choose your preferred interface and enjoy analyzing mobile phone reviews! 📱✨**