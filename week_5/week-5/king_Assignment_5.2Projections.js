// Adds a new user to user's collection.

db.users.insertOne({
  firstName: "Robert",
  lastName: "King",
  employeeId: "1013",
  email: "robaking@example.com"
})

// Verifies that a new user was added to collection by using firstName of new user.

db.users.find({ firstName: "Robert" })

//  Updates and existing users email address.

db.users.updateOne ({ firstName: "Wolfgang", lastName: "Mozart" })
{ $set: { email: "mozart@me.com" }}

// Verifies that updated users email address was updated correctly.

db.users.find({ firstName: "Wolfgang", lastName: "Mozart" })

// Displays all users in the collection using projections to display first name, last name, and email.

db.users.find({}, { firstName: 1, lastName: 1, email: 1, _id: 0})