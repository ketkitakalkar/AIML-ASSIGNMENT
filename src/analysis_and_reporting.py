import os
import pandas as pd
from collections import Counter

def analyze_trends(data):
    """
    Analyze trends in categorized issues by counting occurrences of each category.
    """
    category_counts = data['category'].value_counts().to_dict()
    return category_counts

def extract_common_keywords(data, category):
    """
    Extract common keywords from issue titles within a specific category.
    """
    selected_data = data[data['category'] == category]
    all_titles = " ".join(selected_data['Title'].dropna()).lower().split()
    keyword_counts = Counter(all_titles).most_common(10)
    return keyword_counts

def generate_insights(data):
    """
    Generate insights based on the most frequent issue category.
    """
    most_common_category = data['category'].value_counts().idxmax()
    insights = {}
    if most_common_category == "bug":
        insights["message"] = "Frequent bugs suggest gaps in testing or quality control."
    elif most_common_category == "documentation":
        insights["message"] = "Many documentation issues indicate unclear or incomplete instructions."
    elif most_common_category == "feature request":
        insights["message"] = "Numerous feature requests may highlight unmet user needs."
    elif most_common_category == "compatibility":
        insights["message"] = "Compatibility issues suggest mismatched dependencies or unsupported environments."
    insights["most_common_category"] = most_common_category
    return insights

def generate_report(data, output_path):
    """
    Generate a structured report summarizing trends, keywords, and root cause insights.
    """
    # Start building the report
    report_lines = []
    report_lines.append("# Root Cause Analysis Report")
    report_lines.append("\n## Issue Trends")
    
    # Analyze trends
    category_counts = analyze_trends(data)
    for category, count in category_counts.items():
        report_lines.append(f"- {category}: {count} issues")
    
    # Analyze keywords for the most frequent category
    insights = generate_insights(data)
    most_common_category = insights["most_common_category"]
    report_lines.append(f"\n## Common Keywords in '{most_common_category}' Issues")
    keyword_counts = extract_common_keywords(data, most_common_category)
    for word, count in keyword_counts:
        report_lines.append(f"- {word}: {count} times")
    
    # Add root cause insights
    report_lines.append("\n## Root Cause Analysis Insights")
    report_lines.append(f"- {insights['message']}")
    
    # Write the report to a file
    with open(output_path, 'w') as report_file:
        report_file.write("\n".join(report_lines))
    print(f"Report saved to {output_path}")

if __name__ == "__main__":
    # Define paths
    data_file = "../data/categorized_issues.csv"
    report_file = "../data/root_cause_analysis_report.md"
    
    # Load issue data
    if os.path.exists(data_file):
        issues = pd.read_csv(data_file)
        
        # Generate and save the report
        generate_report(issues, report_file)
    else:
        print(f"Error: Data file '{data_file}' not found.")
