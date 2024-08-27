from threading import *
from time import *
from re import *

start = perf_counter()
listdict = {}
def perform_operation(gg):
    match_obj = match(r'(\d+)([/*+-])(\d+)', gg)
    if match_obj:
        num1, operator, num2 = match_obj.groups()
        num1 = int(num1)
        num2 = int(num2)
        if operator == '/':
            return num1 // num2
        elif operator == '*':
            return num1 * num2
        elif operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
    else:
        print(f"No match found for: {gg}")
        return None

def MandD():
    results = []
    for num in range(len(examples)):
        gg = "".join(examples[num].split())
        pattern = r"(\d+[/*]\d+)"
        matches = finditer(pattern, gg)
        listdict[num] = list(gg)
        #print(listdict)
        for match in matches:
            start_index = match.start()
            end_index = match.end()
            matched_string = match.group()
            #print(f"Matched pattern '{matched_string}' found at indices [{start_index}, {end_index}]")
            result = perform_operation(matched_string)
            results.append(result)
    #print(results)
    listdict[0][2:5] = [str(results[0])]
    listdict[0][4:] = [str(results[1])]
    listdict[1][0:4] = [str(results[2])]
    listdict[1][4:] = [str(results[3])]
    listdict[2][2:5] = [str(results[4])]
    listdict[2][4:] = [str(results[5])]
    #print(listdict)


def A():
    results = []
    for num in range(len(listdict)):
        gg = "".join(listdict[num])
        pattern = r"(\d+[+]\d+)"
        matches = findall(pattern, gg)
        #print(matches)
        for gg in matches:
            result = perform_operation(gg)
            results.append(result)
    #print(results)
    listdict[0][0:3] = [str(results[0])]
    listdict[1][0:3] = [str(results[1])]
    listdict[2][2:] = [str(results[2])]
    #print(listdict)

def S():
    results = []
    for num in range(len(listdict)):
        gg = "".join(listdict[num])
        pattern = r"(\d+[-]\d+)"
        matches = findall(pattern, gg)
        #print(matches)
        for gg in matches:
            result = perform_operation(gg)
            results.append(result)
    #print(results)
    listdict[0][0:] = [str(results[0])]
    listdict[1][0:] = [str(results[1])]
    listdict[2][0:] = [str(results[2])]
    #print(listdict)
    for num in range(len(listdict)):
        print(f'example {num + 1} : {listdict[num][0]}')

examples = ["3 + 5 * 2 - 6 / 3", "10 * 2 + 5 - 8 / 2", "4 - 6 / 3 + 8 * 2"]
#MandD()
#A()
#S()

x = Thread(target=MandD)
x.start()
y = Thread(target=A)
y.start()
z = Thread(target=S)
z.start()

x.join()
y.join()
z.join()

print(active_count())
print(enumerate())
finish = perf_counter()
print(f"Finished in {round(finish-start, 5)} second(s)")
