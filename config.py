from configparser import ConfigParser
import os

def create_config():
    config = ConfigParser()
    config["Settings"] = {
        "Token" : "change me",
        "DefaultChannel": "change me"
    }
    if os.path.isfile("./config.cfg"):
        os.rename("./config.cfg", "./config.cfg.old")
    with open("./config.cfg", "w") as file:
        config.write(file)


def read_config():
    parser = ConfigParser()
    parser.read("config.cfg")
    return parser["Settings"]["Token"], parser["Settings"]["DefaultChannel"]

if __name__ == "__main__": 
    create_config()
