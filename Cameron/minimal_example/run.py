import os

import Cameron.Cameron.BOFS.create_app
from Cameron.Cameron.BOFS.create_app import create_app

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app")
app = create_app(path, 'minimal.cfg')

if __name__ == '__main__':
    app.run(host="0.0.0.0")