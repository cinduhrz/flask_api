## const express = require("express")
import flask
## const HomeRouter = require("...")
from controllers import routes

## Create Flask App
## const app = express()
app = flask.Flask(__name__)

## app.use(HomeRouter)
app.register_blueprint(routes)

## Run Server
## app.listen(PORT, () => {})
app.run(port=4000)