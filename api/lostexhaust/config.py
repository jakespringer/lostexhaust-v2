import os, json

conf = None
with open(os.path.join(os.path.dirname(__file__), "..", "..", "conf", "config.json"), "r") as config_file:
  conf = json.loads(config_file.read())
  conf["rootDir"] = os.path.abspath(os.path.join(__file__, "..", ".."))
  if conf is None:
    print("There was an error reading the config file. LostExhaust could not be started.")

def get(str):
    return conf[str]
