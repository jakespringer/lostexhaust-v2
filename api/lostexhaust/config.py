import os, json

conf = None
with open("/usr/local/lostexhaust/lostexhaust/conf/config.json", "r") as config_file:
  conf = json.loads(config_file.read())
  conf["rootDir"] = "/usr/local/lostexhaust/lostexhaust/api"

def get(str):
    return conf[str]
