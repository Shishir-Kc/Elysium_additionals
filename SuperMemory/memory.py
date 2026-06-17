from pathlib import Path
import os 
import logging 
from datetime import datetime
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
    def read_memory_config(self):
        pass
    def create_memory_lane(self):
        logger.info("Creating memory lane ")
   


memory = SuperMemory()
memory.create_memory_lane()
