# from bark import SAMPLE_RATE, generate_audio, preload_models
# from scipy.io.wavfile import write as write_wav
# from IPython.display import Audio
# import os, math, random

# os.environ["SUNO_ENABLE_MPS"] = "True"
# os.environ["SUNO_OFFLOAD_CPU"] = "True"
# os.environ["SUNO_USE_SMALL_MODELS"] = "True"
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# # download and load all models
# preload_models()

# # generate audio from text
# text_prompt = """
#   Dreams are the blueprint of your destiny, and success is the masterpiece you create from it.
# """

# audio_array = generate_audio(text_prompt,voice_preset = "v2/en_speaker_6")

# # save audio to disk
# write_wav("bark_g.wav", SAMPLE_RATE, audio_array)


import os
import pandas as pd
from transformers import AutoProcessor, BarkModel
from scipy.io.wavfile import write as write_wav

# Setup environment variables
os.environ["SUNO_ENABLE_MPS"] = "True"
os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# Load the processor and model
processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")

# Define the voice preset
voice_preset = "v2/en_speaker_0"

# Load your CSV file
# df = pd.read_csv("/Users/burnaboy/Desktop/FREELANCE/PANAMA PAPER/LE MILLION/LEVEL UP/CSV/short_quotes.csv")
df = pd.read_csv("/Users/burnaboy/Desktop/FREELANCE/PANAMA PAPER/LE MILLION/LEVEL UP/SCRIPT/Clipper/short_quotes.csv")

for index, row in df.iterrows():
    theme, text = row['Theme'], row['Text']
    # Ensure the theme directory exists
    theme_dir = os.path.join(os.getcwd(), theme)
    os.makedirs(theme_dir, exist_ok=True)

    # Process the text with the specified voice preset
    inputs = processor(text, voice_preset=voice_preset)

    # Generate audio from the processed text
    outputs = model.generate(**inputs)
    audio_array = outputs.cpu().numpy().squeeze()

    # Define the sample rate
    sample_rate = model.generation_config.sample_rate

    # Define the output path, using the index for the filename
    output_path = os.path.join(theme_dir, f"{index}.wav")

    # Save the audio file
    write_wav(output_path, sample_rate, audio_array)

    print(f"Generated audio saved to: {output_path}")

