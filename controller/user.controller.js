const User = require("../models/user.model");
const jwt = require("jsonwebtoken");

module.exports.signup = (req, res) => {
  const { name, email, password, role } = req.body;
  const newUser = new User({ name, email, password, role });

  newUser
    .save()
    .then((user) => {
      return res.status(200).json({
        data: user,
        success: true,
        error: null,
      });
    })
    .catch((err) => {
      return res.status(400).json({
        data: null,
        success: false,
        error: err.message,
      });
    });
};

module.exports.login = (req, res) => {
  const { email, password } = req.body;
  User.findOne({ email: email }).then((user) => {
    if (!user) {
      return res
        .status(400)
        .json({ message: "User is not registered with us" });
    }
    if (password != user.password) {
      return res.status(400).json({ message: "invalid password" });
    }

    //jwtt sign
    jwt.sign(
      { _id: user.id },
      process.env.JWTKEY,
      { expiresIn: 3600 },
      (err, token) => {
        return res.status(200).json({
          token,
          data: { name: user.name, email: user.email },
          success: true,
        });
      }
    );
  });
};
