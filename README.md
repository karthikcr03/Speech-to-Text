# 🎤 Speech-to-Text with Whisper 🤖

This project uses OpenAI's **Whisper** model to transcribe audio files (e.g., MP3) into text and store the results in both `.txt` and `.json` formats. You can easily convert speech into text and store the transcription for later use or further processing. 💬🎶

## 🚀 Project Overview

- **Audio File**: The audio file (`tina.mp3`) is loaded and processed to fit a 30-second duration.
- **Whisper Model**: The Whisper model (small version) is used to detect the spoken language and transcribe the speech to text.
- **Output**: The transcribed text is saved as both a `.txt` file and a `.json` file for easy integration into other applications.

## 🛠️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/speech-to-text-whisper.git
    cd speech-to-text-whisper
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have an audio file (e.g., `tina.mp3`) in the project directory for transcription. 🎧


## 🔧 Script Descriptions

### 1. `speechtotext.py` 📝
This script performs the following:
- Loads the audio file (`tina.mp3`).
- Pads or trims the audio to ensure it's 30 seconds long.
- Converts the audio into a log-Mel spectrogram.
- Detects the language of the spoken text.
- Transcribes the speech into text using the Whisper model.
- Saves the transcription to both a `.txt` file and a `.json` file.

### 2. `text_to_json.py` 📄
- Converts the transcribed text from `speechtotext.py` into a structured JSON format for better integration into other systems.

### 3. `whispy_script.py` 🧪
An alternate script that might have additional features or temporary test code for experimentation.

## 🧠 How It Works

1. **Load Audio** 🎧:
   - The audio file `tina.mp3` is loaded and processed using Whisper.
   - It is padded or trimmed to fit a 30-second duration, ensuring that the audio is ready for transcription.

2. **Language Detection** 🌍:
   - Whisper automatically detects the language spoken in the audio based on the log-Mel spectrogram.

3. **Transcription** 🗣️:
   - The Whisper model transcribes the speech and converts it into readable text.

4. **Saving Transcriptions** 💾:
   - The transcribed text is saved in two formats:
     - `.txt` file for human-readable transcription.
     - `.json` file for structured data that can be easily integrated into applications.

## 🔥 Run the Script

To transcribe the audio and save the results:

1. Run the `speechtotext.py` script:
    ```bash
    python speechtotext.py
    ```

2. After running the script, check the following output files:
    - **`transcription.txt`**: Contains the plain text transcription.
    - **`transcription.json`**: Contains the transcription in a structured JSON format.

## 📦 Dependencies

- **whisper**: OpenAI's Whisper model for speech-to-text transcription.
- **json**: To handle JSON file operations.
- **os**: For file system operations.

Install dependencies with:
```bash
pip install whisper


