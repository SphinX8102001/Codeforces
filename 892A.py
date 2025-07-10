import sys

NoOfCans = int(sys.stdin.readline().strip())
ListOfRemainingVolsInCans = sys.stdin.readline().strip().split()
ListOfRemainingVolsInCans = [int(x) for x in ListOfRemainingVolsInCans]
ListOfCapacitiesOfCans = sys.stdin.readline().strip().split()
ListOfCapacitiesOfCans = [int(x) for x in ListOfCapacitiesOfCans]
ListOfCapacitiesOfCans.sort()
totalCapacityOfCans = ListOfCapacitiesOfCans[-1] + ListOfCapacitiesOfCans[-2]
TotalRemainingVols = 0

for remainingCapacity in ListOfRemainingVolsInCans:
    TotalRemainingVols += remainingCapacity

if totalCapacityOfCans >= TotalRemainingVols:
    print("YES")
else:
    print("NO")    
