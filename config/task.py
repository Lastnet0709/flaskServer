from flaskServer.entity.taskData import TaskData
from flaskServer.entity.taskAccount import TG
from flaskServer.entity.taskData import TaskChain

objects = {
    'multifarm': TaskData,
    "telegram": TG,
    "Onenesslabs": TaskData,
    "NowChain": TaskChain,

}

def get_object_by_name(name):
    return objects.get(name)