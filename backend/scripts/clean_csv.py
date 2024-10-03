import pandas as pd

# Path to your CSV file
file_path = './train_dataset.csv'  # Update this with the path to your CSV
cleaned_file_path = './cleaned_train_dataset.csv'  # Update this with your desired path

# Initialize an empty list to hold the chunks of cleaned data
cleaned_chunks = []

# Define the chunk size
chunk_size = 1000  # Number of rows per chunk

try:
    # Read the CSV file in chunks
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        # Remove duplicates from the current chunk
        cleaned_chunk = chunk.drop_duplicates()
        # Append the cleaned chunk to the list
        cleaned_chunks.append(cleaned_chunk)
        print(f"Processed chunk with {len(cleaned_chunk)} rows. Total processed: {len(cleaned_chunks)*chunk_size}")

except Exception as e:
    print(f"Error reading the CSV file: {e}")

# Combine all cleaned chunks into a single DataFrame
df_cleaned = pd.concat(cleaned_chunks, ignore_index=True)

# Remove any duplicates across the entire dataset after concatenation
df_cleaned = df_cleaned.drop_duplicates()

# Save the cleaned data to a new CSV file
try:
    df_cleaned.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned dataset saved to: {cleaned_file_path}")
except Exception as e:
    print(f"Error saving the cleaned CSV file: {e}")
