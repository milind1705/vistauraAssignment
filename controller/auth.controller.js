const User = require("../models/user.model");
module.exports.adminRoutes = async (req, res) => {
  const userid = req.payload._id;
  const user = await User.findById(userid);
  const role = user.role;
  if (user.role == "admin") {
    return res.status(200).json("This is admin routes");
  } else {
    return res.status(400).json("YOnly admin can access this routes");
  }
};

module.exports.employeeRoutes = async (req, res) => {
  return res.status(200).json("This is employee routes");
};
