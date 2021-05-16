import sys

terminator="\n"
reverse=False
sparator= " "
for i,each in enumerate(sys.argv[1:]):
    if each =="-n":
        terminator = ""
    elif each=="-r":
        reverse=True
    elif each=="-l":
        sparator="\n"
    else:
        break

args=sys.argv[i+1:]
if reverse:
    args=reversed(args)

print(sparator.join(args),end=terminator)
