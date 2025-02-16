/*
Title: kingAggregateQueries.js
Author: Robert King
Date: February 16, 2025
Description: Queries for performing various operations on houses and students collections using MongoDB Shell.
*/

// Select the database to use.
use("web335DB");

// a. Display all students.
db.students.find().pretty();

// b. Add a new student
newStudent = {
  "firstName": "Robert",
  "lastName": "AKing",
  "studentId": "s1019",
  "houseId": "h1007"
};
db.students.insertOne(newStudent);

/*
b. Alternative (easier to implement in MongoDB Shell)
db.students.insertOne({"firstName":"Robert", "lastName":"AKing", "studentId":"s1019", "houseId":"h1007"});
*/

// Prove the new student was successfully added.
db.students.find({ "studentId": "s1019" }).pretty;

// c. Update one property from the added student.
db.students.updateOne(
  { "studentId": "s1019" },
  { $set: { "lastName": "King" }}
);

// Prove the student was successfully updated.
db.students.find({ "studentId": "s1019" }).pretty();

// d. Delete the newly created student from step b.
db.students.deleteOne({ "studentId": "s1019" });

// Prove the student was successfully deleted.
db.students.find({ "studentId": "s1019" }).pretty();

// e. Display all students by house (Display house then students).
db.houses.aggregate([
  { $lookup: {
    from: "students",
    localField: "houseId",
    foreignField: "houseId",
    as: "students"
  }}
]).pretty();

// f. Display all students in house Gryffindor (Display house then students).
db.houses.aggregate([
  { $match: { houseId: "h1007"}},
  { $lookup: {
    from: "students",
    localField: "houseId",
    foreignField: "houseId",
    as: "students"
  }}
]).pretty;

// g. Display all students in the house with the Eagle mascot (Display house then students).
db.houses.aggregate([
  { $match: { mascot: "Eagle" }},
  { $lookup: {
    from: "students",
    localField: "houseId",
    foreignField: "houseId",
    as: "students"
  }}
]).pretty();