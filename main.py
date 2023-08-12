import random

workingDays=5
periodsInADay=10
maxBlockPeriods=3
subjects=5

#calculating how can we distribute 10 periods into block periods
def calculateWays(d,a,t,p,distributionWays):
    for i in a:
        if sum(p)+i<t:
            x=p.copy()
            x.append(i)
            if d+1<=subjects:
                calculateWays(d+1,a,t,x,distributionWays)
        if sum(p)+i==periodsInADay and d==subjects:
            x=p.copy()
            x.append(i)
            distributionWays.append(x)

distributionWays=[]
calculateWays(1,range(1,maxBlockPeriods+1),periodsInADay,[],distributionWays)

random.shuffle(distributionWays)

#streams offered and weekly classes requirementss
streams={"pcmce":{"phy":10,"chem":9,"maths":14,"comp":11,"eng":6}}

chosenDistribution=distributionWays[:5]
chosenStream="pcmce" #provide a method to change in gui

stream=streams[chosenStream]

weekPlan=[] #weekly plan of all subjects starting from the subject requiring the highest number of days

for kk in range(len(list(streams.keys())[0])):
    d=[]
    for i in range(0,len(chosenDistribution)):
        x=chosenDistribution[i].copy()
        d.append(max(x))
        x.remove(max(x))
        chosenDistribution[i]=x
    weekPlan.append(d)

excessClasses=[] #Tracking which subject got either more or less classes
classesAssigned=[sum(x) for x in weekPlan]

classesRequired=sorted(list(stream.values()))[::-1] #Required classes from max to min
correspondingSubs=sorted(stream,key=lambda x: stream[x])[::-1]

excessClasses=[classesAssigned[i]-classesRequired[i] for i in range(len(classesAssigned))] #calculating how many classes excess or less are there

for i in range(len(excessClasses)):
    if excessClasses[i]:
        sch=weekPlan[i]
        while excessClasses[i]!=0:
            for i in range(len(sch)):
                
    else:
        pass