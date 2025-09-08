import os
from dotenv import load_dotenv
load_dotenv()




class Credentials:
    STAGE = os.getenv("STAGE", "dev")

    if STAGE == "dev":
        LOGIN = os.getenv("DEV_LOGIN")
        PASSWORD = os.getenv("DEV_PASSWORD")





