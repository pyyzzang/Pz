import threading
import time

class Task():
    StartTask = None
    TaskThread = None

    @staticmethod
    def AppendTask(addTask):
        if(None == Task.StartTask):
            Task.StartTask = addTask
            Task.RunTask()
        else:
            findTask = Task.StartTask
            while(None != findTask.NextTask):
                findTask = findTask.NextTask
            findTask.NextTask = addTask
    
    @staticmethod
    def DeleteTask(removeTask):
        if(removeTask == Task.StartTask):
            Task.StartTask = Task.StartTask.NextTask
        else:
            findTask = Task.StartTask
            while(removeTask != findTask.NextTask):
                findTask = findTask.NextTask
                
            findTask.NextTask = findTask.NextTask.NextTask

    @staticmethod
    def RunTask():
        t = threading.Thread(target=Task.ExecuteTaskThread)
        t.start()
        
    @staticmethod
    def ExecuteTaskThread():
        while(True):
            if(None == Task.StartTask):
                return
            Task.StartTask.Run()
            time.sleep(3)

    def __init__(self):
        self.NextTask = None
        
    def Run(self):
        if(True == self.IsComplete()):
            Task.DeleteTask(self)
        self.NextWork()
    def NextWork(self):
        if(None != self.NextTask):
            self.NextTask.Run()
    
    def IsComplete(self):
        return True

Task.AppendTask(Task())