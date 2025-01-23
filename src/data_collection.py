import requests
import pandas as pd

def collect_issues():
    url = 'https://api.github.com/repos/octocat/Hello-World/issues'  

    response = requests.get(url)

    if response.status_code == 200:
        issues_data = response.json()  
        
        issues = []
        for issue in issues_data:
            if isinstance(issue, dict): 
                issues.append({
                    'Issue ID': issue['id'],
                    'Title': issue['title'],
                    'State': issue['state'],
                    'Created At': issue['created_at'],
                    'Updated At': issue['updated_at'],
                    'Labels': ', '.join([label['name'] for label in issue.get('labels', [])]),
                })
            else:
                print(f"Skipping invalid data: {issue}")

        return pd.DataFrame(issues)
    else:
        print(f"Failed to fetch issues. Status code: {response.status_code}")
        return pd.DataFrame()  # Return an empty DataFrame in case of failure

def main():
    df_issues = collect_issues()
    if not df_issues.empty:
        df_issues.to_csv('../data/issues_data.csv', index=False)  # Save to CSV in the parent directory
        print("Issues data has been saved to 'issues_data.csv'.")
    else:
        print("No issues to save.")

if __name__ == "__main__":
    main()
