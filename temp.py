#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 12:30:55 2023

@author: akromic
"""

import os, math, random
#Import library for text manipulation and display audio
from IPython.display import Audio
import nltk  # we'll use this to split into sentences
nltk.download('punkt')
import numpy as np
#Import SunoAI Bark for text to audio conversion
from bark.generation import (
    generate_text_semantic,
    preload_models,
)
from bark.api import semantic_to_waveform
from bark import generate_audio, SAMPLE_RATE
from scipy.io.wavfile import write as write_wav

# os.environ["SUNO_ENABLE_MPS"] = "True"
os.environ["SUNO_ENABLE_MPS"] = "True"
os.environ["SUNO_OFFLOAD_CPU"] = "True"
# os.environ["SUNO_USE_SMALL_MODELS"] = "True"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

preload_models()


script = """
    Life is an ocean of possibilities. Life is an ocean of possibilities.
""".replace("\n", "").strip()

sentences = nltk.sent_tokenize(script)

GEN_TEMP = 1
SPEAKER = "v2/en_speaker_7"
silence = np.zeros(int(0.08 * SAMPLE_RATE))  # quarter second of silence

pieces = []
for sentence in sentences:
    semantic_tokens = generate_text_semantic(
        sentence,
        history_prompt=SPEAKER,
        temp=GEN_TEMP,
        min_eos_p=0.05,  # this controls how likely the generation is to end
    )

    audio_array = semantic_to_waveform(semantic_tokens, history_prompt=SPEAKER,)
    pieces += [audio_array, silence.copy()]

output_file_path = "bark_generation.wav"
write_wav(output_file_path, SAMPLE_RATE, audio_array)




