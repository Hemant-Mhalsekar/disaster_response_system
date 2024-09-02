def preprocess_data(raw_data):
    # Mock preprocessing (e.g., tokenization, stopword removal)
    for entry in raw_data:
        entry['text'] = entry['text'].lower()  # Simplified preprocessing
    return raw_data

def categorize_data(processed_data):
    # Mock categorization (e.g., using keywords or a simple classifier)
    categories = {
        "flood": "Flood",
        "earthquake": "Earthquake"
    }
    
    for entry in processed_data:
        for keyword, category in categories.items():
            if keyword in entry['text']:
                entry['category'] = category
                break
        else:
            entry['category'] = "Unknown"
    return processed_data
