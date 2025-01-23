import pandas as pd
import os
from transformers import pipeline

# Use the absolute path to load the CSV file (adjusted for the new location)
csv_file_path = r'C:\Users\91950\Desktop\root-cause-analysis\data\issues_data.csv'

# Load issue data
df = pd.read_csv(csv_file_path)

# Load pre-trained model for issue classification (You can use BERT or any LLM)
classifier = pipeline("zero-shot-classification")

# Define categories for issues
categories = ["bug", "feature request", "compatibility", "documentation"]

# Analyze each issue and categorize it
def categorize_issue(issue):
    result = classifier(issue, candidate_labels=categories)
    return result['labels'][0]

df['category'] = df['Title'].apply(categorize_issue)

# Ensure the output directory exists (adjusted for saving inside the src/data folder)
output_dir = r'C:\Users\91950\Desktop\root-cause-analysis\data'
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

# Save categorized issues to a new CSV file with an absolute path
output_file_path = os.path.join(output_dir, 'categorized_issues.csv')
df.to_csv(output_file_path, index=False)

print(f'Categorized issues have been saved to {output_file_path}')
