import sys

def searchForRing(file):
  try:
    f = open(r"files/" + files[i], "r")
    for ln in f:
      line = ln.rstrip()
      for c in range(len(line)):
        if line[c] == charLook:
          return [c, file]
  except:
    print("bad things happened")
  return False

charLook = input()
files = []
file = ""
while file != "END":
  file = input()
  files.append(file)

for i in range(len(files) - 1):
  search = searchForRing(i)
  if search:
    fileName = files[i][0:-4]
    print(f"Found the ring! It was {fileName} at ({search[0]},{search[1]})")
