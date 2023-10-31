import os
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Initialize lists for lines and patterns
lines = []
patterns = []

# Load the data from the generated txt files
folder_path = "hypotactic_txts_greek"
for file_name in os.listdir(folder_path):
    with open(os.path.join(folder_path, file_name), 'r') as f:
        for line in f:
            line_text, line_pattern = line.strip()[1:-1].split('], [')
            lines.append(line_text)
            patterns.append(line_pattern.replace(" ", ""))

# Tokenization for lines
tokenizer = Tokenizer(char_level=True, oov_token='UNK')
tokenizer.fit_on_texts(lines)
vocab_size = len(tokenizer.word_index) + 1
sequences = tokenizer.texts_to_sequences(lines)
padded_sequences = pad_sequences(sequences, padding='post')

# Tokenization for patterns ('u' -> 0, '-' -> 1)
pattern_sequences = [[0 if ch == 'u' else 1 for ch in pattern] for pattern in patterns]
padded_patterns = pad_sequences(pattern_sequences, padding='post')

# Model architecture
model = keras.Sequential([
    keras.layers.Embedding(vocab_size, 64, mask_zero=True),
    keras.layers.LSTM(64, return_sequences=True),
    keras.layers.TimeDistributed(keras.layers.Dense(2, activation='softmax'))
])

# Model compilation
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Reshape labels for training
padded_patterns = np.expand_dims(padded_patterns, -1)

# Training
model.fit(padded_sequences, padded_patterns, epochs=10, batch_size=32)

# Prediction function
def predict_syllable_pattern(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, padding='post')
    pred = model.predict(padded_sequence)
    pred_label = np.argmax(pred, axis=-1)
    pred_pattern = ''.join(['u' if label == 0 else '-' for label in pred_label[0]])
    return pred_pattern.strip('0')

# Test the prediction
print(predict_syllable_pattern("Ἥκω Διὸς παῖς τήνδε Θηβαίαν χθόνα"))
