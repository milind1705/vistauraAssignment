const router = require("express").Router();

const user = require("../controller/user.controller");

router.post("/signup", user.signup);
router.post("/login", user.login);

module.exports = router;
