const express = require("express");
const router = express.Router();
const suggest = require("../controler/suggest_answer")


router.post("/",suggest)
