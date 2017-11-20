class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *num):
        for ind in num:
            if type(ind) == int or type(ind) == float:
                self.result += ind
            else:
                for x in ind:
                    self.result += x

        return self

    def subtract(self, *num):
        for ind in num:
            if type(ind) == int or type(ind) == float:
                self.result += ind
            else:
                for x in ind:
                    self.result += x

        return self


md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
print md.add([1], 3,4).add([3,5,7,8], (2,4.3,1.25)).subtract(2, [2,3], [1.1,2.3]).result
