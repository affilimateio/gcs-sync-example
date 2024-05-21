from google.cloud import storage
import os

# Replace these variables with your own values
service_account_path = 'yourcompany-affilimate.json'
bucket_name = 'yourcompany-affilimate'
dest_file_name = 'www.publisherdomain.com/YYYY-MM-DD-2.csv'
csv_content = 'id,product,amount\n1,Sneakers,70.00\n2,TShirt,25.00'

def upload_csv_to_gcs():
    # Set the environment variable to specify the service account file
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_path

    # Initialize the Google Cloud Storage client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # Create a temporary file to hold the CSV content
    temp_file_path = 'temp.csv'
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write(csv_content)

    # Create a blob object from the file path
    blob = bucket.blob(dest_file_name)

    # Upload the file to the bucket
    blob.upload_from_filename(temp_file_path)

    print(f'CSV file uploaded to {bucket_name}/{dest_file_name}')

    # Clean up the temporary file
    os.remove(temp_file_path)

# Call the function
if __name__ == '__main__':
    upload_csv_to_gcs()
