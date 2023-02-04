## const router = require("express").Router
from flask import Blueprint

## const router = Router()
routes = Blueprint("home", __name__)

## app.get("/", () => {home: "this it the..."}) 
@routes.get("/")
def home():
    return {"home": "this is the home route"}