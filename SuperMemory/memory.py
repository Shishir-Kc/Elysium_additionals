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
from time import sleep
from pydantic import BaseModel
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
ROOTMEMORYPATH = HOMEDIR/".config/E.L.Y.S.I.U.M/Memory"

os.makedirs(MEMORYCONFPATH,exist_ok=True)


class importStuff(BaseModel):
    to_notify:list[str]
    important_tasks:dict[str,str]
    

class MemorySchemaDay(BaseModel):
    title:str
    description:str
    day:str
    summary:str
    emotion:str
    importants:list[importStuff]

class SummarySchema(BaseModel):
    period_type: str# it can either be MONth / year / or weeek 
    period_label: str       # "Week 25, 2026" | "June 2026" | "2026"
    start_date: str
    end_date: str
    title: str
    summary: str
    highlights: list[str]
    emotion_trend: str
    completed_tasks: dict[str, str]
    pending_tasks: list[str]
    lessons: list[str]

class ChatSchema(BaseModel):
    role:str
    content:str

class Message(BaseModel):
    message:list[ChatSchema]


class SuperMemory:
    def __init__(self):
        self.year = self.get_current_year()
        self.month = self.get_current_month()
        self.week = self.get_current_week()
        self.day = self.get_current_day() 

    
    def get_current_year(self):
        logger.info("Getting current year")
        return datetime.now().year
    
    def get_current_month(self):
        return date.today().strftime("%B")
    
    def get_current_day(self):
        return datetime.now().strftime("%d")

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
       
    def log(self,memory:MemorySchemaDay):
        log_path = f"{ROOTMEMORYPATH}/{self.year}/{self.month}/w{self.week}/day{self.day}/log.json"
        with open(log_path,'w') as file:
            json.dump(memory,file,indent=2)

    
    def save_message(self,message:Message):
        chat_path = f"{ROOTMEMORYPATH}/{self.year}/{self.month}/w{self.week}/day{self.day}/chat.json"
        with open(chat_path,'r') as file:
            data = Message.model_validate(json.load(file))
        if isinstance(message,str):
            message = Message.model_validate_json(message)
        elif isinstance(message,dict):
            message = Message.model_validate(message)

        data.message.extend(message.message)
   
        with open(chat_path,"w") as file:
            json.dump(data.model_dump(),file,indent=2)
    def initiatememory(self):
        directory_path = f"{ROOTMEMORYPATH}/{self.year}/{self.month}/w{self.week}/day{self.day}"
        logger.info("Creating memory dir  ")
        os.makedirs(directory_path,exist_ok=True)
        logger.info(f"Dir Path : {directory_path}")
        


memory = SuperMemory()
memory.initiatememory()
data = """
{
  "message": [
    {
      "role": "user",
      "content": "Hello!"
    }
  ]
}
"""
memory.save_message(message=data) #type:ignore

