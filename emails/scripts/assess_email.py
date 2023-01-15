import csv

def assess_emails(file_path):
    # Open the email data file
    with open(file_path, 'r') as file:
        # Read the file as a CSV
        email_data = csv.reader(file)
        # Initialize variables to store email statistics
        total_emails = 0
        spam_emails = 0
        marketing_emails = 0
        for row in email_data:
            total_emails += 1
            if row[2] == 'spam':
                spam_emails += 1
            elif row[2] == 'marketing':
                marketing_emails += 1
                if 'unsubscribe' in row[3].lower():
                    marketing_emails += 1
        # Calculate the percentage of spam emails
        spam_percent = (spam_emails / total_emails) * 100
        #Calculate the percentage of marketing emails
        marketing_percent = (marketing_emails / total_emails) * 100
        print(f'Total emails: {total_emails}')
        print(f'Spam emails: {spam_emails} ({spam_percent:.2f}%)')
        print(f'Marketing emails: {marketing_emails} ({marketing_percent:.2f}%)')
        print(f'Marketing emails with unsubscribe: {marketing_emails} ({marketing_percent:.2f}%)')

if __name__ == '__main__':
    # Assess the emails in the "emails.csv" file
    assess_emails('emails/data/emails.csv')
