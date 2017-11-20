from datetime import datetime

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0

    def get_queue_size(self):
        self.queue = len(self.calls)
    
    def add(self, call):
        self.calls.append(call)
        self.get_queue_size()
        return self

    def remove(self):
        del self.calls[0]
        self.get_queue_size()
        return self

    def remove_number(self,number):
        for x in range(0, len(self.calls)):
            if self.calls[x].number == number:
                print "Deleting number: ", number
                del self.calls[x]
                self.get_queue_size()
                return self
        print "Number not found"
        return self

    def order_queue(self):
        self.calls.sort(key=lambda x: x.time)
        return self

    def info(self):
        print "Queue Lenght: ", self.queue
        for call in self.calls:
            call.display()
        


class Call(object):
    CALL_id = 1
    def __init__(self, id, name, number, time, reason):
        self.id = Call.CALL_id
        self.name = name
        self.number = number
        self.time = datetime.now()
        self.reason = reason
    
        Call.CALL_id += 1

    def display(self):
        print "Call {}: Name: {}, Number: {}, Time: {}, Reason: {}".format(self.id, self.name, self.number, self.time, self.reason)

myCallCenter = CallCenter()
myCallCenter.add(Call(1, "John", "123-123-1234", "1:06", "Inquiry"))
myCallCenter.add(Call(2, "Mary", "234-584-8281", "3:42", "Sales"))
myCallCenter.add(Call(3, "Mathew", "858-928-9271", "4:23", "Cancellation"))
myCallCenter.add(Call(4, "Peter", "837-478-4183", "6:18", "Sales"))
myCallCenter.add(Call(5, "Steve", "627-617-2298", "3:18", "Sales"))
myCallCenter.add(Call(6, "Carlos", "344-927-4851", "2:28", "Sales"))
myCallCenter.info()

myCallCenter.remove().remove().info()

myCallCenter.remove_number("837-9478-9181").info()
myCallCenter.remove_number("858-928-9271").info()

myCallCenter.order_queue().info()