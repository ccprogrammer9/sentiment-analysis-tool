import React, { useState } from 'react';
import './App.css'; // Ensure this path is correct

const SentimentAnalyzer = () => {
    const [text, setText] = useState('');
    const [sentiment, setSentiment] = useState('');

    const analyzeSentiment = async () => {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text }),
        });

        const data = await response.json();
        setSentiment(data.sentiment);
    };

    return (
        <div className="SentimentAnalyzer">
            <h2>Sentiment Analysis</h2>
            <textarea
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Enter text here"
                className="SentimentAnalyzer-textarea"
            />
            <button onClick={analyzeSentiment} className="SentimentAnalyzer-button">Analyze</button>
            {sentiment && (
                <p className="result">Sentiment: {sentiment}</p>
            )}
        </div>
    );
};

export default SentimentAnalyzer;
