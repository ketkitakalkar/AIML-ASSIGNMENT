import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the categorized issues data
data_path = r'C:\Users\91950\Desktop\root-cause-analysis\data\categorized_issues.csv'
issues_data = pd.read_csv(data_path)


# Statistical Summary
def print_statistical_summary(data):
    print("Statistical Summary of Issues Data:")
    print("\nCategory Distribution:")
    print(data['category'].value_counts())
    print("\nState Distribution:")
    print(data['State'].value_counts())
    print("\nTop 5 Most Recent Issues:")
    print(data[['Issue ID', 'Title', 'Created At']].head(5))

# Visualization Functions
def plot_category_distribution(data):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x='category', palette='Set2')
    plt.title('Category Distribution')
    plt.xticks(rotation=45)
    plt.show()

def plot_state_distribution(data):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x='State', palette='Set1')
    plt.title('State Distribution')
    plt.xticks(rotation=45)
    plt.show()

def plot_issue_by_creation_date(data):
    plt.figure(figsize=(10, 6))
    data['Created At'] = pd.to_datetime(data['Created At'])
    data.groupby(data['Created At'].dt.date).size().plot(kind='line', marker='o')
    plt.title('Issues by Creation Date')
    plt.ylabel('Number of Issues')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.show()

# Main Function
def analyze_issues():
    print_statistical_summary(issues_data)
    plot_category_distribution(issues_data)
    plot_state_distribution(issues_data)
    plot_issue_by_creation_date(issues_data)

if __name__ == "__main__":
    analyze_issues()
