# 🤖 AI Chatbot

A simple AI-powered chatbot built with Python and Claude API. Ask anything and get intelligent responses instantly.


## ✨ Features

- 💬 Real-time conversational AI responses
- 🧠 Powered by Claude (Anthropic) API
- 🕐 Maintains chat history within a session
- 📱 Clean and minimal chat UI
- ⚡ Fast response time

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.9+ |
| AI Model | Claude API (Anthropic) |
| UI Framework | Streamlit |
| Environment | python-dotenv |

---

## 📁 Project Structure
```
ai-chatbot/
├── app.py               # Main chatbot application
├── .env                 # API keys (not pushed to GitHub)
├── .gitignore           # Ignores .env and cache files
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Mac/Linux
venv\Scripts\activate           # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the root folder:
```
ANTHROPIC_API_KEY=your_api_key_here
```

> Get your API key from [console.anthropic.com](https://console.anthropic.com)

### 5. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📦 requirements.txt
```
streamlit
anthropic
python-dotenv
```

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Your Anthropic Claude API key |

> ⚠️ Never push your `.env` file to GitHub!

---

## 🧠 How It Works

1. User types a message in the chat input
2. Message is sent to Claude API with full conversation history
3. Claude returns a response
4. Response is displayed in the chat window
5. History is maintained for the entire session

---

## 🗺️ Roadmap

- [x] Basic chatbot with Claude API
- [ ] Add system prompt customization
- [ ] Add multilingual support (Hindi + English)
- [ ] Deploy on Streamlit Cloud
- [ ] Add conversation export feature

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repo
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Your Name**  
[GitHub](https://github.com/Melody5star) • [LinkedIn]([https://linkedin.com/in/your-profile](https://www.linkedin.com/in/anamika-bajpai-54673482/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BgG1n4nDYTlG6DADHqqQsJA%3D%3D))

---

⭐ If you found this useful, please give it a star!
