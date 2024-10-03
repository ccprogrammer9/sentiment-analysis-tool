import React, { useState } from 'react';

function SentimentAnalyzer() {
    const [inputText, setInputText] = useState('');
    const [sentiment, setSentiment] = useState('');

    const analyzeSentiment = async () => {
        try {
            const response = await fetch('http://localhost:5000/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: inputText }),
            });
            const data = await response.json();
            setSentiment(data.sentiment);
        } catch (error) {
            console.error('Error analyzing sentiment:', error);
        }
    };

    return (
        <div className="sentiment-analyzer">
            <input
                type="text"
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                placeholder="Enter a sentence about train travel"
            />
            <button onClick={analyzeSentiment}>Analyze Sentiment</button>
            {sentiment && <p>Sentiment: {sentiment}</p>}
        </div>
    );
}

export default SentimentAnalyzer;
