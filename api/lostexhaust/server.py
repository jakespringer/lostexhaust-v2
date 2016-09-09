import sys, os, config, crypto, traceback
NEW_PATH = os.path.join(config.get("rootDir"))
if not NEW_PATH in sys.path:
    sys.path.append(NEW_PATH)
sys.modules['Crypto'] = crypto

import lostexhaust
from lostexhaust.routes import api

should_run = True

if __name__ == '__main__':
    while should_run:
        try:
            lostexhaust.app.run()
            should_run = False
        except:
            traceback.print_exc()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~         UH OH, SOMETHING BAD HAPPENED.          ~~')
            print('~~ THE SERVER CRASHED AND RESTARTED AUTOMATICALLY. ~~')
            print('~~ CHECK YOUR LOG TO SEE A DETAILED ERROR MESSAGE. ~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
