const router = require("express").Router();

const auth = require("../controller/auth.controller");
const checkAuth = require("../middleware/checkAuth");

router.get("/admin", checkAuth, auth.adminRoutes);
router.get("/emp", checkAuth, auth.employeeRoutes);
module.exports = router;
