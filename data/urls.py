import os
from dotenv import load_dotenv
load_dotenv()


STAGE = os.getenv("STAGE")
class Urls:

    HOST = f"https://{STAGE}-admin.local.com"
