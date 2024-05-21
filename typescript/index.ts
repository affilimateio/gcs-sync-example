import { Storage } from "@google-cloud/storage";
import * as path from "path";
import * as fs from "fs";

// Replace these variables with your own values
const serviceAccountPath = "yourcompany-affilimate.json";
const bucketName = "yourcompany-affilimate";
const destFileName = "www.publisherdomain.com/YYYY-MM-DD.csv";
const csvContent = "id,product,amount\n1,Sneakers,70.00\n2,TShirt,25.00";

// Create a new Google Cloud Storage client using the service account JSON file
const storage = new Storage({
  keyFilename: serviceAccountPath,
});

// Function to upload CSV content to a Google Cloud Storage bucket
async function uploadCsvToGCS() {
  // Create a temporary local file to hold the CSV content
  const tempFilePath = path.join(__dirname, "temp.csv");
  fs.writeFileSync(tempFilePath, csvContent);

  // Upload the file to the bucket
  await storage.bucket(bucketName).upload(tempFilePath, {
    destination: destFileName,
  });

  console.log(`CSV file uploaded to ${bucketName}/${destFileName}`);

  // Clean up the temporary file
  fs.unlinkSync(tempFilePath);
}

// Call the function
uploadCsvToGCS().catch(console.error);
