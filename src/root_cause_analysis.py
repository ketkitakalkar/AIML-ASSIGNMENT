import pandas as pd
import matplotlib.pyplot as plt

# Path to the markdown file (root cause analysis report)
md_file_path = 'C:/Users/91950/Desktop/root-cause-analysis/data/root_cause_analysis_report.md'

# Try reading the markdown file
try:
    with open(md_file_path, 'r') as file:
        md_content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{md_file_path}' was not found. Please check the file path.")
    exit()

# Print the first 500 characters of the markdown content to see its structure
print("First 500 characters of the markdown content:")
print(md_content[:500])

# Check for keywords (just as an example of analysis) in the markdown content
keywords = ['root cause', 'documentation', 'bug', 'feature request', 'compatibility']

# Count the occurrence of each keyword in the markdown content
keyword_counts = {keyword: md_content.lower().count(keyword) for keyword in keywords}

# Display the count of each keyword
print("\nKeyword Counts in the Markdown Report:")
for keyword, count in keyword_counts.items():
    print(f"{keyword}: {count}")

# Visualize the keyword distribution using a bar plot
plt.figure(figsize=(10, 6))
plt.bar(keyword_counts.keys(), keyword_counts.values(), color='skyblue')
plt.title('Keyword Distribution in Root Cause Analysis Report')
plt.xlabel('Keywords')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
