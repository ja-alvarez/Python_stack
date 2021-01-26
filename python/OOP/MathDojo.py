class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result +=num
        for a in nums:
            self.result += a
        return self

    def subtract(self, num, *nums):
        self.result -=num
        for a in nums:
            self.result -= a
        return self

md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x) #5
x= md.add(7).add(4,7).add(12,1).result
print(x) #5+31=36
x=md.subtract(3,4).subtract(1,2).subtract(5).result
print(x) #36-15=21

# lo que sería igual a:
# x = md.add(2).add(2,5,1).subtract(3,2).add(7).add(4,7).add(12,1).subtract(3,4).subtract(1,2).subtract(5).result
#print(x) output:21