import os
import re
import operator
import math
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\input.txt',"r")

monkeys = []

while True:
    monkey = {}
    text = f.readline().strip()
    if not text:
        break
    monkeyRegex = re.match("Monkey (.*):.*",text)
    monkey['number'] = monkeyRegex.group(1)
    print(f"Reading monkey number {monkey['number']}")
    
    text = f.readline().strip()
    startingItemsRegex = re.match("Starting items: (.*)",text)
    monkey['items'] = startingItemsRegex.group(1).split(", ")
    
    text = f.readline().strip()
    operationRegex = re.match("Operation: new = (.*)",text)
    monkey['operation'] = operationRegex.group(1)
    
    text = f.readline().strip()
    testRegex = re.match("Test: divisible by (.*)",text)
    monkey['test'] = testRegex.group(1)
    
    text = f.readline().strip()
    trueRegex = re.match("If true: throw to monkey (.*)",text)
    monkey['trueCase'] = trueRegex.group(1)
    
    text = f.readline().strip()
    falseRegex = re.match("If false: throw to monkey (.*)",text)
    monkey['falseCase'] = falseRegex.group(1)

    monkey['inspections'] = 0

    text = f.readline().strip()

    monkeys.append(monkey)


for round in range(0,20):
    for monkey in monkeys:
        for item in monkey['items']:
            currValue = int(item)
            monkey['inspections'] += 1

            # Calcolo nuovo livello di preoccupazione
            op = monkey['operation'].split(" ")
            operator = ops[op[1]]
            val1 = currValue if op[0] == "old" else int(op[0])
            val2 = currValue if op[2] == "old" else int(op[2])
            newValue = operator(val1,val2)

            # Si abbassa il livello di preoccupazione
            newValue = math.floor(newValue / 3)
            
            # Verifica criterio
            divisibility = int(monkey['test'])
            test = newValue % divisibility == 0
            if test:
                monkeyToThrow = int(monkey['trueCase'])
                newMonkey = monkeys[monkeyToThrow]
                newMonkey['items'].append(str(newValue))
            else:
                monkeyToThrow = int(monkey['falseCase'])
                newMonkey = monkeys[monkeyToThrow]
                newMonkey['items'].append(str(newValue))
        monkey['items'] = []
    
    print()
    print(f"ROUND {round+1}")
    for monkey in monkeys:
        print(f"Monkey {monkey['number']}-> {monkey['items']}")

def sortingFunc(obj):
    return obj['inspections']

monkeys.sort(key=sortingFunc, reverse=True)
affari = monkeys[0]['inspections'] * monkeys[1]['inspections']
print(f"AFFARI: {affari}")