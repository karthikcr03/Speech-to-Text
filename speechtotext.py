
import whispy

model = whispy.load_model("base")

# Load audio and pad/trim it to fit 30 seconds
audio = whispy.load_audio("C:/Users/karth/grandma.mp3")
audio = whispy.pad_or_trim(audio)

# Make log-Mel spectrogram and move to the same device as the model
mel = whispy.log_mel_spectrogram(audio).to(model.device)

# Detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# Decode the audio
options = whispy.DecodingOptions(fp16=False)
result = whispy.decode(model, mel, options)

# Print the recognized text
print(result.text)