from deta import Deta 
import os
from dotenv import load_dotenv


def clone_database(project_key: str):
    deta = Deta(project_key)
    olddb = deta.Base('monkey')
    newdb = deta.Base('development')
    old_data = olddb.fetch()
    print(type(old_data.items))
    for item in old_data.items:
        newdb.insert(item)

load_dotenv()
project_key = os.getenv("PROJECT_KEY")
clone_database(project_key)