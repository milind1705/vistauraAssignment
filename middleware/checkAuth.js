const jwt = require("jsonwebtoken");

module.exports = (req, res, next) => {
  try {
    const { authorization } = req.headers;
    console.log(req.headers);
    const token = authorization.replace("Bearer ", "");
    const decoded = jwt.verify(token, process.env.JWTKEY);
    req.payload = decoded;
    next();
    
  } catch (err) {
    return res.status(401).json("Unauthorized");
  }
};
