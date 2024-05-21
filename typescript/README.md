## Step 1. Install required packages

```node
npm install
```

## Step 2. Modify the script to your company name

Inside index.ts you'll find the following values:

```typescript
const serviceAccountPath = "yourcompany-affilimate.json";
const bucketName = "yourcompany-affilimate";
const destFileName = "www.publisherdomain.com/YYYY-MM-DD.csv";
const csvContent = "id,product,amount\n1,Sneakers,70.00\n2,TShirt,25.00";
```

Replace "yourcompany" with your company name, and "publisherdomain" with the domain of the publisher you're working with.

## Step 3. Run the script

```node
npm run start
```
