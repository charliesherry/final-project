import sys
sys.path.append("src")

import fridge_controllers
from app import app



PORT = 5000
app.run("0.0.0.0", PORT, debug=True)