const fs = require('fs');
const csv = require('fast-csv');
const { MongoClient } = require('mongodb');

// Read CSV file
const csvData = [];
fs.createReadStream("./demographics.csv")
  .pipe(csv.parse({ headers: true }))
  .on('data', (row) => {
    // Process CSV rows
    csvData.push(row);
  })
  .on('end', () => {
    // Connect to MongoDB
    MongoClient.connect('mongodb://localhost:27017', { useNewUrlParser: true, useUnifiedTopology: true }, (err, client) => {
      if (err) throw err;

      const db = client.db('your_database'); // Replace 'your_database' with your database name
      const collection = db.collection('your_collection'); // Replace 'your_collection' with your collection name

      // Insert data into MongoDB collection
      collection.insertMany(csvData, (insertErr, result) => {
        if (insertErr) throw insertErr;
        console.log(`${result.insertedCount} documents inserted`);
        client.close(); // Close MongoDB connection
      });
    });
  });
