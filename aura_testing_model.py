"""
AURA Virtual Assistant - Model Testing Script
"""

import json
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np

with open("aura_training_data.json") as file:
    data = json.load(file)

model = load_model("aura_chat_model.h5")

with open("aura_tokenizer.pkl", "rb") as f:
    tokenizer=pickle.load(f)

with open("aura_label_encoder.pkl", "rb") as encoder_file:
    label_encoder=pickle.load(encoder_file)

while True:
    input_text = input("Enter your command-> ")
    padded_sequences = pad_sequences(tokenizer.texts_to_sequences([input_text]), maxlen=20, truncating='post')
    result = model.predict(padded_sequences)
    tag = label_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            print(np.random.choice(i['responses']))
