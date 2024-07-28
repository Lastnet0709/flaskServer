from flaskServer.mode.task_record import TaskRecord
from flaskServer.config.connect import db,app
from sqlalchemy import and_

def getTaskRecord(env,name):
    with app.app_context():
        taskRecord = TaskRecord.query.filter(and_(TaskRecord.env_name==env,TaskRecord.name==name)).first()
        return taskRecord

def updateTaskRecord(env,name,status):
    taskRecord = getTaskRecord(env,name)
    with app.app_context():
        if taskRecord:
            if taskRecord.status != status:
                taskRecord.status = status
        else:
            taskRecord = TaskRecord(name=name,env_name=env,status=status)
        db.session.add(taskRecord)
        db.session.commit()
        print(f"{env}新增一条{name}任务记录,状态：'{'完成' if status == 0 else '未完成'}'，id：",taskRecord.id)
        return taskRecord

def updateTaskStatus(name,status):
    with app.app_context():
        db.session.query(TaskRecord).filter(TaskRecord.name==name).update({TaskRecord.status:status})
        db.session.commit()

if __name__ == '__main__':
    updateTaskStatus("multifarm",1)