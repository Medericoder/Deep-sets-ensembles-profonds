import sys

class NotSet:

    def __init__(self,value):
        self.value = value

    def dep(self):
        return 0
    
    def mem(self,notset2):
        return False
    
    def __eq__(self,notset2):
        return self.value == notset2.value

class Object:

    def __init__(self,*items):
        self.items = items

    def dep(self):
        if type(self.items) == NotSet:
            return 0
        else:
            memory = 0
            for i in self.items:
                x = i.dep()
                if x > memory:
                    memory = x
            return memory + 1       
        
    def mem(self,object2):
        if type(self.items) == NotSet:
            return False
        else:
            if type(object2) == NotSet:
                for i in self.items:
                    if type(i) == NotSet:
                        if i.value == object2.value:
                            return True
                return False
            elif type(object2) == Object:
                for i in self.items:
                    if type(i) == Object:
                        memory = True
                        for j in i.items:
                            if not(j in object2.items):
                                memory = False
                        if memory:
                            for k in object2.items:
                                if not(k in i.items):
                                    memory = False        
                            if memory:
                                return True
                return False
            else:
                print("Error: some values in the set are incorrect.", sys.exc_info()[0])
                raise
                
    def __eq__(self,object2):
        memory = True
        for i in self.items:
            if not(object2.mem(i)):
                memory = False
        if memory:
            for j in object2.items:
                if not(self.mem(j)):
                    memory = False        
            if memory:
                return True
        return False
        
            





        
        
        
