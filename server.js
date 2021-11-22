require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const port = 3000;
const app = express();
const userRouter = require("./routes/user.routes");
const authRoutes = require("./routes/auth.routes");

//databse connection
mongoose.connect("mongodb://localhost:27017/newAssignment");

mongoose.connection.once("open", () => {
  console.log("connected with database..");
});

//middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

//routing
app.use("/user", userRouter);
app.use("/auth", authRoutes);
//listning
app.listen(port, () => {
  console.log(`server is running on port ${port}`);
});
