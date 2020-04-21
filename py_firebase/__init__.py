import pyrebase
from py_firebase.config import config


firebase = pyrebase.initialize_app({
    "apiKey": config['apiKey'],
    "authDomain": config['authDomain'],
    "databaseURL": config['databaseURL'],
    "storageBucket": config['storageBucket'],
    "serviceAccount": config['serviceAccount']
})
