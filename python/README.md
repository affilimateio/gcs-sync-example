## Step 1. Install required packages

```
pip install -r requirements.txt
```

## Step 2. Modify the script to your company name

Inside main.py you'll find the following values:

```python
service_account_path = 'yourcompany-affilimate.json'
bucket_name = 'yourcompany-affilimate'
dest_file_name = 'www.publisherdomain.com/YYYY-MM-DD-2.csv'
csv_content = 'id,product,amount\n1,Sneakers,70.00\n2,TShirt,25.00'
```

Replace "yourcompany" with your company name, and "publisherdomain" with the domain of the publisher you're working with.

## Step 3. Run the script

```python
python main.py # or python3 main.py
```
