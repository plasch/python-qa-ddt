from allpairspy import AllPairs

data = [
    ["DELL", "ACER", "ASUS"],
    ["WIN7", "XP", "WIN10"],
    ["AMD", "INTEL", "ARM"],
    ["CHROME", "FIREFOX", "IE11"]
]

pairwised_result = AllPairs(data)

for i, pairs in enumerate(pairwised_result):
    print(i+1, pairs)

print("=" * 20)

i = 1
for comp in data[0]:
    for oper in data[1]:
        for proc in data[2]:
            for browser in data[3]:
                print(i, [comp, oper, proc, browser])
                i = i + 1
