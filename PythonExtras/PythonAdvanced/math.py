class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *vals):
        for val in vals:
            if isinstance(val, int):
                self.total += val

            else:
                for i in val:
                    self.total += i                    
        return self

    def substract(self, *vals):
        for val in vals:
            if isinstance(val, int):
                self.total -= val

            else:
                for i in val:
                    self.total -= i                    
        return self

    def result(self):
        print self.total


md = MathDojo()

md.add(3, 3, (1, 1)).result()
md.add(2).add(2,5).substract(3,2).result()
MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).substract(2, [2,3], [1.1, 2.3]).result()