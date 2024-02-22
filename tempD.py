#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 12:30:55 2023

@author: akromic
"""

import os, math, random

os.environ["CUDA_VISIBLE_DEVICES"] = "0"


#Import library for text manipulation and display audio
from IPython.display import Audio
import nltk  # we'll use this to split into sentences
import numpy as np
#Import SunoAI Bark for text to audio conversion
from bark.generation import (
    generate_text_semantic,
    preload_models,
)
from bark.api import semantic_to_waveform
from bark import generate_audio, SAMPLE_RATE



script = """
    Life is an ocean of possibilities, and at the heart of navigating its vastness is self-belief.
    Self-belief is the wind in your sails; it's what propels you forward when the waters get rough. 
    It's not just about believing that you can do something; it's about knowing that you already have the power within you to achieve it. 
    Every challenge you face is an opportunity to prove to yourself just how much you're capable of. 
    Your potential is like a dormant volcano; it's always been there, just waiting for the right moment to erupt into something magnificent. 
    Believe in that inner strength. Trust in your ability to overcome obstacles. 
    With self-belief, you're not just moving forward; you're soaring to new heights. 
    Let your self-belief be your compass, guiding you through uncharted waters to shores of success you never thought possible. 
    Remember, the belief in oneself is the first step on the ladder of achievement. 
    Climb that ladder with confidence and watch as you turn your dreams into reality.
""".replace("\n", "").strip()
    

if __name__ == "__main__" :
    pass
    # preload_models()
    # sentences = nltk.sent_tokenize(script)
    

    