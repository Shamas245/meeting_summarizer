
# 📝 Meeting Summarizer

**Meeting Summarizer** is a **Streamlit-based Python application** that streamlines meeting documentation by processing audio, video, or transcript files to generate professional summaries, action items, and downloadable Word documents. It leverages **Whisper** (for transcription) and **Gemini** (for text analysis), and integrates with **Slack** for seamless team collaboration.

---

## 🚀 Features

* **📁 File Uploads:** Accepts `.mp4`, `.wav`, `.mp3`, or `.txt` files with size validation.
* **🔊 Audio Extraction & Transcription:** Extracts audio from videos using `moviepy` and transcribes using **Whisper**.
* **🧠 AI Summarization:** Uses **Gemini** to generate smart, meeting-type-specific summaries and action items.
* **📄 Document Export:** Generates `.docx` reports using `python-docx` with summary, action items, and transcript.
* **💬 Slack Integration:** Sends summaries and action items directly to a Slack channel via webhook.
* **🎛️ Clean UI:** Built with Streamlit with tabs, dropdowns, collapsible views, and progress indicators.
* **🛡️ Error Handling:** Friendly error messages, logs (`app.log`), and temporary file cleanup.

---

## 📦 Prerequisites

* Python 3.8+
* [FFmpeg](https://ffmpeg.org/) installed and added to your system path
* A valid **Gemini API key**
* A **Slack webhook URL**

---

## ⚙️ Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/meeting-summarizer.git
   cd meeting-summarizer
   ```

2. **Create Virtual Environment (Optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   **Example `requirements.txt`:**

   ```txt
   streamlit==1.30.0
   python-dotenv==1.0.0
   whisper==0.7.0
   google-generativeai==0.5.0
   moviepy==1.0.3
   python-docx==1.1.0
   librosa==0.10.0
   requests==2.31.0
   numpy==1.24.0
   ```

4. **Install FFmpeg**

   * macOS: `brew install ffmpeg`
   * Ubuntu: `sudo apt-get install ffmpeg`
   * Windows: [Download from FFmpeg](https://ffmpeg.org/download.html) and add to PATH

---

## 🔐 Configuration

1. **Environment Variables**

   Create a `.env` file in the root directory:

   ```env
   SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/webhook/url
   GEMINI_API_KEY=your-gemini-api-key
   ```

2. **Configuration File: `config.py`**

   Ensure the following settings exist in `config.py`:

   ```python
   MAX_FILE_SIZE_MB = 200
   WHISPER_MODEL = "base"
   GEMINI_MODEL = "gemini-pro"
   AUDIO_CONFIG = {
       "supported_video_formats": ["mp4", "mov", "avi"],
       "supported_audio_formats": ["wav", "mp3"]
   }

   ERROR_MESSAGES = {
       "file_too_large": "File size exceeds {max_size}MB limit.",
       "empty_transcript": "Uploaded transcript is empty.",
       "slack_error": "Failed to send to Slack."
   }

   SUCCESS_MESSAGES = {
       "file_uploaded": "File uploaded successfully!",
       "processing_complete": "Processing complete!",
       "slack_sent": "Sent to Slack successfully!"
   }

   UI_CONFIG = {
       "max_transcript_display": 1000
   }

   SUMMARIZATION_PROMPT = "Summarize the following meeting transcript: {transcript}"
   ACTION_ITEMS_PROMPT = "Extract action items from the following transcript: {transcript}"

   MEETING_TYPE_PROMPTS = {
       "general": {
           "summary": SUMMARIZATION_PROMPT,
           "actions": ACTION_ITEMS_PROMPT
       },
       "standup": {
           "summary": "Summarize this daily standup meeting: {transcript}",
           "actions": "List team updates and blockers: {transcript}"
       },
       "planning": {
           "summary": "Summarize this planning meeting: {transcript}",
           "actions": "Extract upcoming tasks and responsibilities: {transcript}"
       },
       "retrospective": {
           "summary": "Summarize this retrospective: {transcript}",
           "actions": "Highlight improvements and action points: {transcript}"
       }
   }
   ```

---

## 🧪 Usage

### Run the App

```bash
streamlit run main.py
```

### Open in Browser

Visit [http://localhost:8501](http://localhost:8501)

---

## 🖥️ How to Use

1. **Choose a Meeting Type**
   (e.g., General, Standup, Planning, Retrospective)

2. **Upload a File**

   * Video (`.mp4`)
   * Audio (`.wav`, `.mp3`)
   * Transcript (`.txt`)

3. **Click "Process Meeting"**
   AI will extract text, generate a summary, and identify action items.

4. **Review Results**

   * Summary
   * Action Items
   * Full Transcript (collapsible)

5. **Download & Share**

   * Download `.docx` report
   * Send to Slack via button

---

## 📁 File Structure

```text
meeting-summarizer/
│
├── main.py               # Core Streamlit app
├── config.py             # App configuration settings
├── slack.py              # Slack integration logic
├── .env                  # Environment variables (not committed)
├── app.log               # Logging for debug/tracking
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## ❗ Troubleshooting

| Issue                                 | Solution                                            |
| ------------------------------------- | --------------------------------------------------- |
| **Missing `config.py` or `slack.py`** | Ensure both files exist with correct settings.      |
| **File size error**                   | Check `MAX_FILE_SIZE_MB` in `config.py`.            |
| **Slack not working**                 | Confirm the webhook URL is correct and valid.       |
| **Audio not processing**              | Make sure `ffmpeg` is installed and in system path. |
| **API errors**                        | Check if Gemini API key is active and has access.   |

---

## 🤝 Contributing

We welcome contributions!
Please open an issue or submit a pull request for suggestions, bugs, or feature improvements.

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for more details.
