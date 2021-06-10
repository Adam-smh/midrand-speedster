km = int(input("What was your Average speed?"))
limit = int(input("What was the speed limit?"))

print("")

if km <= limit:
    print("OK")

elif km > limit:
    points = (km - limit)/5
    print("Points:",  int(points))
    if int(points) > 12:
        print("Jail time")
