/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
use("web335DB");

// Display all users in the collection
db.users.find({});

// Display the user with email address jbach@me.com
db.users.findOne({ "email": "jbach@me.com" });

// Display the user with the last name Mozart
db.users.findOne({ "lastName": "Mozart" });

// Display the user with first name Richard
db.users.findOne({"firstName": "Richard" });

// Display the user with employeeId 1010
db.users.findOne({ "employeeId": "1010" });