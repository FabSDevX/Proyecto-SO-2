from dotenv import load_dotenv
#.env
load_dotenv()

class Config:
    PORT = 5001
    HOST = '0.0.0.0'
    DEBUG = True