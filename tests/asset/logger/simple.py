from core4.config.tool import connect

mongo_database = "core4test"

logging = {
    "mongodb": "DEBUG"
}

kernel = {
    "sys.log": connect("mongodb://sys.log")
}