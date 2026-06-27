# 🎬 YouTube Sentiment Analysis

> **Analyze and understand the sentiment of YouTube video comments using AI-powered insights!**

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [✨ Key Features](#-key-features)
- [📦 Prerequisites](#-prerequisites)
- [⚙️ Setup Instructions](#️-setup-instructions)
- [🚀 Usage Guide](#-usage-guide)
- [📁 Project Structure](#-project-structure)
- [🔧 Configuration](#-configuration)
- [📝 API Keys Setup](#-api-keys-setup)
- [📊 Output](#-output)
- [🛠️ Technology Stack](#️-technology-stack)
- [👤 Author](#-author)
- [📄 License](#-license)

---

## 🎯 Project Overview

**YouTube Sentiment Analysis** is an intelligent Python application that analyzes and reports the sentiment of comments on any YouTube video. It leverages Google's Gemini AI to process up to 100 of the newest comments and provides:

- ✅ **Sentiment Classification** - Categorizes comments as positive, negative, or neutral
- 📊 **Detailed Statistics** - Counts and percentages for each sentiment category
- 📝 **Comment Summaries** - Grouped summaries by sentiment type
- 🔍 **Trend Analysis** - Identifies notable patterns and trends in audience sentiment
- 📄 **Markdown Reports** - Professional, well-formatted output reports

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🤖 **AI-Powered Analysis** | Uses Google Gemini 3.1 Flash Lite for intelligent sentiment detection |
| 📹 **YouTube Integration** | Seamless connection to YouTube API for real-time comment retrieval |
| 🎨 **Formatted Output** | Generates clean markdown reports automatically |
| 🔐 **Secure** | API keys stored safely in environment variables |
| 📦 **Easy Setup** | Poetry-based dependency management |

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.14+** (Ensure compatibility with your system)
- **Poetry** (Python package manager) - [Install Poetry](https://python-poetry.org/docs/#installation)
- **Git** (for version control)

### Installation Check

```bash
# Verify Python installation
python --version

# Verify Poetry installation
poetry --version
```

---

## ⚙️ Setup Instructions

### Step 1️⃣: Clone the Repository

```bash
git clone https://github.com/Ritz97/Youtube-Sentiment-Analysis.git
cd Youtube-Sentiment-Analysis
```

### Step 2️⃣: Install Dependencies

Use Poetry to install all required dependencies:

```bash
poetry install
```

This command reads the `pyproject.toml` file and installs:
- `python-dotenv` - Environment variable management
- `google-api-python-client` - YouTube API client
- `google-genai` - Google Gemini AI integration
- `pyyaml` - YAML configuration parsing

### Step 3️⃣: Create Environment Configuration

Create a `.env` file in the project root directory:

```bash
# Using touch (Linux/Mac)
touch .env

# Or create manually and add the following content
```

Add your API keys to the `.env` file (see [API Keys Setup](#-api-keys-setup) below):

```env
YOUTUBE_API_KEY=your_youtube_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### Step 4️⃣: Verify Setup

```bash
# Activate the Poetry environment
poetry shell

# Test imports (optional)
python -c "import googleapiclient; import google.genai; print('✅ All dependencies loaded successfully!')"
```

---

## 🚀 Usage Guide

### Running the Application

```bash
# From the project directory
poetry run python src/main.py
```

### Step-by-Step Execution

1. **Start the program:**
   ```bash
   poetry run python src/main.py
   ```

2. **Enter a YouTube Video ID:**
   ```
   Enter the YouTube video ID: dQw4w9WgXcQ
   ```
   > 💡 **Tip:** Find the Video ID in the YouTube URL: `youtube.com/watch?v=[VIDEO_ID]`

3. **Wait for Analysis:**
   - The program fetches up to 100 newest comments
   - Sends them to Google Gemini for sentiment analysis
   - Processes and analyzes the results

4. **View Results:**
   - Results display in the terminal
   - A formatted markdown file is automatically saved to `./output/Output.md`

### Example Output

```
🎬 YouTube Video Sentiment Analysis Report

📊 Overall Statistics:
- Positive Comments: 67 (67%)
- Negative Comments: 18 (18%)
- Neutral Comments: 15 (15%)

✅ Positive Sentiment Summary:
Users love the production quality and engaging content...

❌ Negative Sentiment Summary:
Some viewers found the video too long and pace unclear...

⚪ Neutral Sentiment Summary:
Comments about video availability and technical aspects...

🔍 Notable Trends:
Strong praise for cinematography throughout comments...
```

---

## 📁 Project Structure

```
Youtube-Sentiment-Analysis/
├── src/                              # Source code directory
│   ├── main.py                       # Main entry point
│   └── util.py                       # Utility functions
├── config/                           # Configuration files
│   └── genai_system_instruction.yaml # AI system prompts
├── output/                           # Generated reports (auto-created)
│   └── Output.md                     # Sentiment analysis results
├── pyproject.toml                    # Poetry configuration & dependencies
├── poetry.lock                       # Locked dependency versions
├── .env                              # Environment variables (create this)
├── .gitignore                        # Git ignore rules
└── README.md                         # This file
```

### File Descriptions

| File | Purpose |
|------|---------|
| `src/main.py` | Entry point that orchestrates the sentiment analysis workflow |
| `src/util.py` | Contains utility functions for YouTube API, AI calls, and file operations |
| `config/genai_system_instruction.yaml` | System instructions for Gemini AI about sentiment analysis requirements |
| `pyproject.toml` | Project metadata and dependencies managed by Poetry |
| `poetry.lock` | Exact versions of installed dependencies (for reproducibility) |

---

## 🔧 Configuration

### System Instructions Customization

The AI's behavior is defined in `config/genai_system_instruction.yaml`:

```yaml
youtube_main_instruction: >-
  You are a helpful assistant
  that analyzes the sentiment of YouTube comments.
  Your task is to read the provided 100 newest comments on a video
  and determine whether the sentiment is positive, negative, or neutral.
  ... [full instructions continue]
```

**To customize analysis:**

1. Open `config/genai_system_instruction.yaml`
2. Modify the `youtube_main_instruction` field
3. Change sentiment categories, output format, or analysis depth
4. Save and re-run the application

### Example Customizations

```yaml
# Add more detailed analysis
youtube_main_instruction: >-
  Analyze comments and categorize as:
  - EXTREMELY_POSITIVE
  - POSITIVE
  - NEUTRAL
  - NEGATIVE
  - EXTREMELY_NEGATIVE
  Include confidence scores for each comment...
```

---

## 📝 API Keys Setup

### 🔑 Getting YouTube API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable the **YouTube Data API v3**
4. Create an **API Key** credential
5. Copy your key to the `.env` file as `YOUTUBE_API_KEY`

### 🤖 Getting Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **"Get API Key"** (or **"Create API Key"**)
3. Copy your key to the `.env` file as `GEMINI_API_KEY`

### ⚠️ Security Best Practices

- **Never commit `.env` files** to version control
- **Rotate keys regularly** for security
- **Use separate keys** for development and production
- **Limit API permissions** in Google Cloud Console
- **Monitor API usage** to detect unauthorized access

---

## 📊 Output

### Output Location

Analysis results are automatically saved to:
```
./output/Output.md
```

The file is created automatically if the `output` directory doesn't exist.

### Output Format

The report is formatted in **Markdown** and includes:

```markdown
# Sentiment Analysis Report

## Summary Statistics
- Positive: X comments
- Negative: Y comments
- Neutral: Z comments

## Sentiment Breakdown
[Detailed summaries for each sentiment category]

## Key Trends
[Notable patterns identified in comments]
```

---

## 🛠️ Technology Stack

```
┌─────────────────────────────────────┐
│  Python 3.14+                       │
├─────────────────────────────────────┤
│  Dependencies:                      │
│  ├─ google-api-python-client       │
│  ├─ google-genai (Gemini AI)       │
│  ├─ python-dotenv                  │
│  └─ pyyaml                         │
├─────────────────────────────────────┤
│  External APIs:                     │
│  ├─ YouTube Data API v3             │
│  └─ Google Gemini 3.1 Flash         │
└─────────────────────────────────────┘
```

---

## 🐛 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| ❌ `ModuleNotFoundError: No module named 'googleapiclient'` | Run `poetry install` to install dependencies |
| ❌ `Invalid Video ID` | Ensure you're using the correct 11-character YouTube video ID |
| ❌ `API quota exceeded` | Wait before making more requests; YouTube API has daily limits |
| ❌ `.env file not found` | Create `.env` file in project root with your API keys |
| ❌ `Authentication failed` | Verify your API keys are correct and enabled in Google Cloud Console |

### Debug Mode

To enable verbose logging, add to `src/main.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 👤 Author

**Ritam De**

- GitHub: [@Ritz97](https://github.com/Ritz97)
- Project: [YouTube Sentiment Analysis](https://github.com/Ritz97/Youtube-Sentiment-Analysis)

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📞 Support & Questions

If you have questions or encounter issues:

1. Check the **Troubleshooting** section above
2. Review the code comments in `src/util.py` and `src/main.py`
3. Open an [Issue](https://github.com/Ritz97/Youtube-Sentiment-Analysis/issues)

---

<div align="center">

### 🌟 If you find this project helpful, please consider starring it! ⭐

**Happy Analyzing! 🎉**

</div>
