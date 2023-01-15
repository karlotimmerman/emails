import csv

def process_emails(file_path):
    # Open the email data file
    with open(file_path, 'r') as file:
        # Read the file as a CSV
        email_data = csv.reader(file)
        # Initialize an empty list to store processed emails
        processed_emails = []
        for row in email_data:
            # Extract the relevant information from the email
            sender = row[0]
            subject = row[1]
            email_type = row[2]
            body = row[3]
            # Perform processing on the email body
            processed_body = body.replace('\n', ' ') # remove newline characters
            processed_body = processed_body.replace('\r', ' ') # remove return characters
            processed_body = processed_body.replace('\t', ' ') # remove tab characters
            processed_body = processed_body.strip() # remove leading and trailing whitespace
            # Append the processed email to the list
            processed_emails.append([sender, subject, email_type, processed_body])
    # Write the processed emails to a new CSV file
    with open('processed_emails.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(processed_emails)

if __name__ == '__main__':
    # Process the emails in the "emails.csv" file
    process_emails('emails/data/emails.csv')
