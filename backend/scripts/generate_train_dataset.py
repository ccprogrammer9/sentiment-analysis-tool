import pandas as pd
import random

def generate_sentences():
    """Generate a list of unique sentences based on sentiment labels."""

    # Base templates for each sentiment
    positive_templates = [
        "I absolutely love traveling by train!",
        "Train journeys provide an unparalleled experience.",
        "Nothing compares to a scenic train ride through the countryside.",
        "The train was not just comfortable; it was luxurious.",
        "Relaxing on a train is my favorite way to spend a day.",
        "Traveling by train offers a wonderful opportunity for reflection.",
        "The views from my train window were simply breathtaking.",
        "Choosing the train for long distances has always been my best decision.",
        "There is something magical about traveling by train.",
        "I always feel a sense of excitement boarding the train."
    ]

    neutral_templates = [
        "The train departed on schedule.",
        "I took the train to visit the city center.",
        "Trains are a well-established mode of transport.",
        "I’ve traveled by train many times.",
        "The train station was quite busy during rush hour.",
        "I watched a train pass through the station.",
        "The train schedule was easy to read.",
        "I found a seat right by the window.",
        "The process of purchasing tickets was seamless.",
        "The announcements made during the trip were clear."
    ]

    negative_templates = [
        "The train was delayed for several hours.",
        "I had an awful experience traveling by train.",
        "The train was overcrowded and extremely uncomfortable.",
        "I would much prefer to drive than take the train.",
        "The train ride was chaotic and loud.",
        "I completely missed my stop on the train.",
        "Technical issues caused a significant delay in our journey.",
        "I encountered rude passengers during my journey.",
        "The food served on the train was way too expensive.",
        "The train was unclean and poorly maintained."
    ]

    # Function to create unique sentences by mixing and matching templates
    def create_unique_sentences(templates, sentiment, count):
        unique_sentences = set()
        while len(unique_sentences) < count:
            base_sentence = random.choice(templates)
            # Create variations of the base sentence
            variation = base_sentence.replace("train", random.choice(["express train", "local train", "bullet train", "commuter train", "sleeper train"]))
            unique_sentences.add(base_sentence)
            unique_sentences.add(variation)

        return [{"text": sentence, "label": sentiment} for sentence in unique_sentences]

    # Generate unique sentences for each sentiment category
    positive_sentences = create_unique_sentences(positive_templates, "positive", 100)
    neutral_sentences = create_unique_sentences(neutral_templates, "neutral", 100)
    negative_sentences = create_unique_sentences(negative_templates, "negative", 100)

    # Combine all sentences
    dataset = positive_sentences + neutral_sentences + negative_sentences
    random.shuffle(dataset)  # Shuffle the dataset to mix the sentiments

    # Create a DataFrame from the dataset
    df = pd.DataFrame(dataset)

    # Drop duplicates to ensure unique sentences
    df = df.drop_duplicates(subset='text')

    # Check if we have enough unique sentences
    unique_count = len(df)

    # Ensure we have at least 1000 unique sentences
    while unique_count < 300:
        label = random.choice(["positive", "neutral", "negative"])
        templates = positive_templates if label == "positive" else neutral_templates if label == "neutral" else negative_templates
        new_sentences = create_unique_sentences(templates, label, 1)
        for sentence in new_sentences:
            if sentence not in df.values:
                df = pd.concat([df, pd.DataFrame([sentence])], ignore_index=True)
        unique_count = len(df)

    return df

# Generate the dataset
dataset = generate_sentences()

# Save the dataset to a CSV file
dataset.to_csv('train_dataset.csv', index=False)
print("Dataset generated and saved to train_dataset.csv")
