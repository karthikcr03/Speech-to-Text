import whisper
import json
model = whisper.load_model("small")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("tina.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)
with open("transcription.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(result.text)



output_data = {"detected_text": result.text}

with open("transcription.json", "w", encoding="utf-8") as json_file:
    json.dump(output_data, json_file, ensure_ascii=False, indent=4)


