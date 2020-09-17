class Stack:
    def __init__(self):
        self.items=[]
        pass

    def push_stack(self,data):
        self.items.append(data)
        pass

    def pop_stack(self):
        return self.items.pop()

    def peak_stack(self):
        return self.items[-1]

    def update_stack(self,index,data):
        self.items[index]=data

