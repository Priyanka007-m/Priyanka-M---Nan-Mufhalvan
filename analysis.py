from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Initialize VADER analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment():
    input_text = entry.get()
    if not input_text.strip():
        messagebox.showwarning("Warning", "Please enter a sentence!")
        return
    
    scores = analyzer.polarity_scores(input_text)
    compound = scores['compound']
    
    if compound >= 0.05:
        sentiment = 'Positive'
    elif compound <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    # Create DataFrame
    df = pd.DataFrame([{
        'Sentence': input_text,
        'Negative': scores['neg'],
        'Neutral': scores['neu'],
        'Positive': scores['pos'],
        'Compound': compound,
        'Sentiment': sentiment
    }])
    
    result_text.set(f"Sentiment: {sentiment}\n\n{df.to_string(index=False)}")

# Create GUI using Tkinter
root = tk.Tk()
root.title("Sentiment Analysis")

# Input Field
tk.Label(root, text="Enter a sentence:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Button to analyze
tk.Button(root, text="Analyze", command=analyze_sentiment).pack(pady=10)

# Output
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.pack(pady=10)

root.mainloop()
