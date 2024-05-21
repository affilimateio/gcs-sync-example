# gcs-sync-example
Send transaction data to Affilimate via GCS.

## Setup
Choose either the Python or TypeScript code examples. Within each directory, you'll find a
README.md with instructions on how to run the code.

For each script, ensure you replace the variables with your own values. For example, in
the Python script:

```python
# Replace these variables with your own values
service_account_path = 'yourcompany-affilimate.json'
bucket_name = 'yourcompany-affilimate'
dest_file_name = 'www.publisherdomain.com/YYYY-MM-DD-2.csv'
csv_content = 'id,product,amount\n1,Sneakers,70.00\n2,TShirt,25.00'
```

You'll want to be sure to replace the `service_account_path` and `bucket_name` with your own
values for testing. Then replace the other variables with your own data, as you proceed with development.

## Testing
You'll see a success message out of the script when the file has been successfully synced.

Let us know which filename to check for, and we'll confirm that the data has been received on our end.
