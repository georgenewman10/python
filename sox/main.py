from datetime import datetime

##schedule = open('schedule.txt', 'r')
copy = open('datacopy.txt', 'r')

by_number = {}
by_team = {}
by_date = {}

#for line in schedule:
    #line = line.rstrip()
    #line = line.split(", ")
    #print(line[4])
    #updated_time = []
    #by_number[line[0]] = line[1:]               # index by game number



for line in copy:
    line = line.rstrip()
    line = line.split(", ")
    line[4] = float(line[4])
    line[4] = line[4] - 1
    line[4] = '%05.2f' % line[4]
    print(line[4])
    by_team[line[0]] = line[1:]


#print(by_number['003'][3])
#print(by_team['003'][3])
