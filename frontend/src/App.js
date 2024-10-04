import React from 'react';
import './App.css';
import SentimentAnalyzer from './SentimentAnalyzer'; // Import the SentimentAnalyzer component
import trainImage from './images/train.jpg'; // Import the train image (update the path as needed)

function App() {
    return (
        <div className="App">
            <header className="App-header">
                {/* Train image for context */}
                <img src={trainImage} alt="A train" className="train-image" />

                {/* Main Title */}
                <h1>Train Travel</h1>

                {/* Tool Subtitle */}
                <h2>Sentiment Analysis Tool</h2>

                {/* Brief description */}
                <p>Type a sentence about train travel below to analyze the sentiment.</p>
            </header>

            {/* SentimentAnalyzer Component */}
            <div className="SentimentAnalyzer">
                <SentimentAnalyzer /> {/* SentimentAnalyzer will follow new CSS rules */}
            </div>
        </div>
    );
}

export default App;
