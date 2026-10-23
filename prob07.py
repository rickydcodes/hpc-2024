#prob03
# n = int(input())
# raw = n / 3.05
# s = str(raw)
# if ("." in s):
#   s = str(round(raw * 10) / 10)
# else:
#   s += ".0"
# print(s)

#prob07
metrics = [5, 4, 3, 2, 1]
values = [0, 0, 0, 0, 0]
data = []
inp = -1
while (inp != 0):
  inp = int(input())
  if (inp != 0):
    data.append(inp)

for n in data:
  for i in range(len(metrics)):
    if (n == metrics[i]):
      values[i] += 1

for i in range(len(metrics)):
  o = str(metrics[i]) + " (" + str(values[i]) + ") |"
  for j in range(values[i]):
    o += "="
  print(o)

avg = (5 * values[0]) + (4 * values[1]) + (3 * values[2]) + (2 * values[3]) + (1 * values[4])
avg /= len(data)

avg = int(avg * 100) / 100
disp = str(avg)
if ("." in disp):
  things = disp.split(".")
  if (len(things[1]) <= 1):
    disp += "0"
else:
  disp += ".00"

print("Average efficiency: " + disp)
