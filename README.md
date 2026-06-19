# AI-Chatbot


```markdown
# ⚡ Groq Lightning Chatbot

A blazing-fast conversational AI chatbot powered by **Groq's ultra-low latency hardware** and **Llama-3.3-70b** model. Built with Streamlit for an interactive, feature-rich experience.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)


## ✨ Features

### 🧠 Core Capabilities
- **Multiple AI Models**: Choose between Llama-3.3-70b, Llama3-8b, and Mixtral-8x7b
- **Real-time Streaming**: See responses generate character by character
- **Conversation Memory**: Persistent chat history throughout your session
- **Customizable Responses**: Control creativity (temperature) and response length

### 📁 PDF Document Chat
- **Multi-PDF Upload**: Chat with multiple documents simultaneously
- **Two Query Modes**:
  - 💬 AI + PDF: Enhanced answers using document context
  - 📄 Only from PDF: Strict answers based solely on documents
- **One-Click Summary**: Generate comprehensive document summaries
- **Smart Context Integration**: AI prioritizes document information when relevant

### 🎤 Voice & Input Features
- **Voice Input**: Speak your prompts using your microphone
- **Text Input**: Traditional chat input with Markdown support
- **Format Options**: Choose response styles (Bullet Points, Step-by-Step, Tables)

### 💾 Chat Management
- **Save Conversations**: Export chat history as JSON files
- **Load Previous Chats**: Resume conversations from saved files
- **Export as Markdown**: Download conversations in clean Markdown format
- **Clear History**: Reset conversation with one click

### 📊 Analytics Dashboard
- **Session Metrics**: Track message counts, character usage, and estimated tokens
- **Response Timing**: See exactly how fast each response generates
- **PDF Statistics**: Monitor uploaded documents and their status

### 🎨 User Experience
- **Typing Indicator**: Visual feedback while AI thinks
- **Copy Button**: Quick copy of AI responses
- **Responsive Design**: Works on desktop and mobile
- **Dark/Light Theme**: Adapts to your Streamlit theme

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A [Groq API Key](https://console.groq.com) (free tier available)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/tanishq-jain124/groq-chatbot.git
cd groq-chatbot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run chatbot.py
```

4. **Enter your API key** in the sidebar when the app loads

### Requirements

Create a `requirements.txt` file with:

```txt
streamlit>=1.28.0
groq>=0.5.0
pypdf>=3.17.0
streamlit-mic-recorder>=0.1.0
```

## 📖 Usage Guide

### 1️⃣ Getting Started
- Launch the app and enter your Groq API key in the sidebar
- Start chatting immediately in the main chat input

### 2️⃣ Using PDF Documents
1. Upload one or more PDFs using the file uploader in sidebar
2. Choose your query mode:
   - **AI + PDF**: General questions enhanced with document context
   - **Only from PDF**: Strict Q&A based only on uploaded documents
3. Click "Generate PDF Summary" for quick document overviews
4. Ask questions about your documents naturally

### 3️⃣ Voice Input
- Click the microphone button in sidebar
- Speak your question clearly
- The text will auto-populate in the chat

### 4️⃣ Advanced Settings
- **Temperature**: 0.0 (focused) to 1.5 (creative)
- **Max Tokens**: Control response length (100-4096)
- **Response Format**: Choose presentation style
- **Model Selection**: Switch between different Groq models

### 5️⃣ Managing Chats
- **Save**: Click "Save Conversation" to export as JSON
- **Load**: Upload a previously saved JSON file
- **Export**: Download as Markdown for documentation
- **Clear**: Reset conversation history

## 🎯 Example Use Cases

| Use Case | How To |
|----------|--------|
| **Research Paper Analysis** | Upload PDFs, use "Only from PDF" mode |
| **Creative Writing** | Set high temperature, use "Default" format |
| **Technical Documentation** | Upload manuals, ask specific questions |
| **Meeting Notes** | Use voice input, export as Markdown |
| **Study Assistant** | Upload textbooks, get bullet-point summaries |
| **Code Documentation** | Use step-by-step format for explanations |

## 🛠️ Technical Architecture

```
┌─────────────────────────────────────────────────────┐
│                 Streamlit Frontend                  │
│  ┌───────────────┐  ┌──────────────────────────┐  │
│  │   Sidebar UI   │  │    Main Chat Interface   │  │
│  │  - API Key     │  │  - Message History       │  │
│  │  - Settings    │  │  - Streaming Responses   │  │
│  │  - PDF Upload  │  │  - Copy/Export Options   │  │
│  │  - Voice Input │  │                          │  │
│  └───────────────┘  └──────────────────────────┘  │
└─────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│                   Groq API Client                   │
│  ┌───────────────────────────────────────────────┐  │
│  │  - Model Selection                           │  │
│  │  - Temperature & Token Control               │  │
│  │  - Streaming Completion                      │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│                Groq Cloud Hardware                  │
│           (Ultra-low latency inference)             │
└─────────────────────────────────────────────────────┘
```

## 🔒 Security

- **API keys are NEVER stored** - they're entered at runtime
- All processing happens in your browser and Groq's cloud
- No data is persisted to any external servers
- PDFs are processed locally in your browser
- Chat history is only saved locally (if you choose to)

## 🐛 Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| **API Key Error** | Ensure you have a valid Groq API key from console.groq.com |
| **PDF Not Processing** | Check PDF is not password-protected or corrupted |
| **Voice Not Working** | Allow microphone permissions in your browser |
| **Slow Responses** | Try a smaller model like `llama3-8b-8192` |
| **Memory Issues** | Clear conversation history or reduce max tokens |

## 🚀 Future Enhancements

- [ ] Image upload and analysis
- [ ] Multi-language support for PDFs
- [ ] Custom system prompts
- [ ] Chat search functionality
- [ ] Export as different formats (CSV, Excel)
- [ ] Collaborative chat rooms
- [ ] API usage statistics
- [ ] Conversation templates

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request




## 🙏 Acknowledgments

- [Groq](https://groq.com) for their incredible low-latency hardware
- [Streamlit](https://streamlit.io) for the amazing framework
- [Llama](https://llama.meta.com) for the powerful language models

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/tanishq-jain124/groq-chatbot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/tanishq-jain124/groq-chatbot/discussions)
- **Groq Documentation**: [Groq Docs](https://console.groq.com/docs)

---

## 📸 Screenshots

*(Add screenshots here after deploying)*
<img width="1918" height="1013" alt="output_chatbot" src="https://github.com/user-attachments/assets/41835841-83a3-4395-9e37-91bc725687a0" />



<details>
<summary>Click to see screenshots</summary>

### Main Interface
![Main Interface](screenshots/main.png)
<img width="1918" height="1013" alt="output_chatbot" src="https://github.com/user-attachments/assets/07854568-d046-4ff7-920e-23e547bccf59" />


### PDF Chat
![PDF Chat](screenshots/pdf.png)

<img width="1918" height="1013" alt="output_chatbot" src="https://github.com/user-attachments/assets/0c680e62-1587-482d-ae6b-7240a6ac6210" />


### Analytics Dashboard


<img width="1918" height="1013" alt="output_chatbot" src="https://github.com/user-attachments/assets/e54f4c47-8d2c-4430-b74e-98362cf7d7c6" />


</details>

---

**Built with ❤️ using Groq's lightning-fast inference**
```

## 📁 Additional Files to Consider

### 1. `requirements.txt`
```txt
streamlit>=1.28.0
groq>=0.5.0
pypdf>=3.17.0
streamlit-mic-recorder>=0.1.0
```

### 2. `.gitignore`
```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
ENV/

# Streamlit
.streamlit/secrets.toml

# Chat files
chat_history_*.json
chat_export_*.md

# IDE
.vscode/
.idea/
*.swp
*.swo



This README provides:
- **Clear project overview** with badges
- **Complete features list** 
- **Installation guide** 
- **Usage instructions** with examples
- **Security information**
- **Troubleshooting guide**
- **Professional formatting** with emojis and sections

You can customize the GitHub URLs and add screenshots once you upload the repo! 🚀
