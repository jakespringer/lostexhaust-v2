import sys, os, config
NEW_PATH = os.path.join(config.get("rootDir"))
if not NEW_PATH in sys.path:
    sys.path.append(NEW_PATH)

import lostexhaust
from lostexhaust.routes import api

if __name__ == "__main__":
    lostexhaust.app.run()
