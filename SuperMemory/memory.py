"""
This code is responsible for E.L.Y.S.I.U.M Memory 
here is the basic structure for the Memory 

 |MemoryRoot:
 |
 | 
 |---- Year2026
 |  |
 |  |
 |  |
 |  |----- June 
 |    |
 |    |
 |    |-----wek26
 |
 """


from pathlib import Path
import os 
import logging 
from datetime import datetime,date
import json

logger = logging.getLogger("SuperMemory.memory")
logging.basicConfig(
    level= logging.DEBUG,
    format= "| %(levelname)s | %(name)s | %(asctime)s| %(message)s",
    handlers=[
        logging.StreamHandler(),
    ]
)
logger.info("Starting SuperMemory")

HOMEDIR=Path.home()
MEMORYCONFPATH = f"{HOMEDIR}/.config/E.L.Y.S.I.U.M/Config/Memory"


os.makedirs(MEMORYCONFPATH,exist_ok=True)


class SuperMemory:
    def __init__(self):
        pass
    
    def get_current_year(self):
        logger.info("Getting current year")
        return datetime.now().year
    
    def get_current_month(self):
        return datetime.now().month
    
    def get_current_week(self):
        """
            This method returns current number of week ,
            as of running this code today is 26th week of year 2026 month 6 

        """
        today = date.today()
        week = int(today.strftime("%V"))
        return week


    def read_memory_config(self):
        pass

    def create_memory_lane(self):
        logger.info("Creating memory lane ")

memory = SuperMemory()
memory.create_memory_lane()
# print(memory.get_current_year(),memory.get_current_month(),memory.get_current_week())
