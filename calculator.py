

class calculator(object) :

    def calculate(self, input):
        a, b = input
        return a / b

    def show_result(self):
        print(res.index(min(res)) + 1)

res = []
c = calculator()
with open('source.txt', 'r+') as fo:
    for line in fo:
        current = [int(i) for i in line.split()]
        res.append(c.calculate(current))
c.show_result()
