'''
TODO
FIGUIRE OUT A WAY TO SUM THE WEEK SCHEDULE INTO PERIODS EACH DAY
'''

import random
from itertools import combinations_with_replacement
import math
import copy

def schedule(periods_per_sub):
    max_block_periods=3
    periods_in_a_day=10
    working_days=5

    def add_period(periods,target,new,possibilities):
        periods=periods.copy()
        periods.append(new)
        #global working_days
        #global max_block_periods
        if sum(periods)==target:
            periods=periods.copy()
            if len(periods)==working_days:
                random.shuffle(periods)
                possibilities.append(periods)
            elif len(periods)<working_days:
                periods.extend((working_days-len(periods))*[0])
                random.shuffle(periods)
                possibilities.append(periods)
            else:
                pass
        elif len(periods)>working_days:
            pass
        else:
            periods=periods.copy()
            for i in range(1,max_block_periods+1):
                add_period(periods,target,i,possibilities)

    def random_scheduler(periods_required):
        #global working_days
        #global max_block_periods
        periods=[]
        possibilites=[]
        for i in range(1,max_block_periods+1):
            add_period(periods,periods_required,i,possibilites)
        return possibilites

    #random scheduler function returns how n number of periods could be divided into all working days


    weekplans=[]
    for key in periods_per_sub:
        weekplans.append(random.choice(random_scheduler(periods_in_a_day)))

    table=copy.deepcopy(weekplans)

    periods={}
    for key in periods_per_sub:
        periods[key]=[]
    #print(weekplans)
    periodTracks=[]
    for key in periods:
        #print(key)
        target=periods_per_sub[key]
        su=0
        periodTrack=[]
        j=0
        while j<len(weekplans):
            x=min(max(weekplans[j]) if len(weekplans[j]) else math.inf,target-su)
            try:
                i=weekplans[j].index(x)
                weekplans[j].pop(i)
                periodTrack.append([j,i])
                su+=x
            except:
                for jj in range(0,len(weekplans)):
                    try:
                        i=weekplans[jj].index(x)
                        weekplans[jj].pop(i)
                        periodTrack.append([jj,i])
                        su+=x
                        break
                    except:
                        pass
            #print(su)
            j+=1
        periodTracks.append(periodTrack)

    #print(periodTracks,len(periodTracks))
    #print(weekplans)
    tt=[[] for i in range(0,working_days)]
    periods_assigned={}
    for key in periods_per_sub:
        periods_assigned[key]=0
    for i in range(0,len(periodTracks)):
        for j in range(0,len(periodTracks[i])):
            #print(periodTracks[i][j][0],list(periods_per_sub.keys())[i])
            z=table[periodTracks[i][j][0]].pop(periodTracks[i][j][1])
            y=list(periods_per_sub.keys())[i]+str(z)
            #print(periodTracks[i][j][0],y)
            periods_assigned[list(periods_per_sub.keys())[i]]+=z
            tt[periodTracks[i][j][0]].append(y)
    #print(weekplans,periods_assigned)
    weekplans=[sum(x) if len(x) else 0 for x in weekplans]
    #print(weekplans)
    for key in periods_per_sub:
        periods_assigned[key]=periods_per_sub[key]-periods_assigned[key]
    #print(periods_assigned)
    #print(weekplans)
    #print("-"*50)
    for key in periods_assigned:
        if periods_assigned[key]!=0:
            for i in range(0,len(weekplans)):
                if weekplans[i]>=periods_assigned[key]:
                    tt[i].append(key+str(periods_assigned[key]))
                    weekplans[i]-=periods_assigned[key]
    #print(weekplans)
    [random.shuffle(x) for x in tt]
    for i in tt:
        j=0
        for k in i:
            j+=int(k[-1])
        if j!=periods_in_a_day:
            return schedule(periods_per_sub)
    return tt


def fitness(arr1,arr2):
    try:
        fit=0
        indices=[]
        for i in range(0,len(arr1)):
            #print(i)
            if arr1[i]!=arr2[i]:
                fit+=1
            else:
                indices.append(i)
        return fit,indices
    except Exception as e:
        print(e)

'''x=schedule({"phy":10,"chem":10,"math":15,"comp":10,"eng":5})
for i in x:
    j=0
    for k in i:
        j+=int(k[-1])
    print(j)
print(x)'''

def final_schedule():
    classes={"pcmc":{"phy":10,"chem":10,"math":15,"comp":10,"eng":5},"pcmb":{"phy":10,"chem":10,"math":15,"bio":10,"eng":5},"pcbpe":{"phy":10,"chem":10,"bio":15,"pe":10,"eng":5},"pcbpsy":{"phy":10,"chem":10,"bio":15,"psy":10,"eng":5}}
    teachers={"phy":["A","B","AA","BB"],"chem":["C","D","CC","DD"],"math":["E","F","EE","FF"],"comp":["G","GG"],"bio":["H","I","HH"],"pe":["J","JJ"],"psy":["K","KK"],"eng":["L","M","N","O"]}
    teachers_given={}
    for key in teachers:
        for j in teachers[key]:
            teachers_given[j]=0

    timetables={}
    teachers_assigned={}
    for key in classes:
        timetables["XII"+key]=schedule(classes[key])
        teachers_assigned["XII"+key]={}
        subs=classes[key]
        for sub in subs:
            aa=random.choice(teachers[sub])
            while teachers_given[aa]>=2:
                teachers[sub].remove(aa)
                aa=random.choice(teachers[sub])
            teachers_given[aa]+=1
            teachers_assigned["XII"+key][sub]=aa
    for key in timetables:
        f=[]
        for e in timetables[key]:
            t=[]
            for g in e:
                t.extend([g[:-1]]*int(g[-1]))
            f.append(t)
        timetables[key]=f
    
    teachers_assignment={}

    for key in timetables:
        tt=timetables[key]
        tt=copy.deepcopy(tt)
        for t in tt:
            for j in range(0,len(t)):
                t[j]=teachers_assigned[key][t[j]]
        teachers_assignment[key]=tt
    print(teachers_assigned)
    final_timetable=[]
    for j in range(0,5):
        first_day=[teachers_assignment[key][j] for key in teachers_assignment]
        perm_assignemnt={}
        for i in range(0,len(first_day)):
            for j in range(i+1,len(first_day)):
                try:
                    score,ind=fitness(first_day[i],first_day[j])
                except:
                    return "failed"
                iterations=0
                while score!=10:
                    iterations+=1
                    if iterations>1000000:
                        print("RESCHEDULING","."*50)
                        return "failed"
                    for z in range(0,len(ind)):
                        teacher=first_day[j][ind[z]]
                        try:
                            av_swaps=list(set(range(0,10))-set(perm_assignemnt[teacher]))
                        except Exception as e:
                            perm_assignemnt[teacher]=[]
                            av_swaps=range(0,10)
                        if len(av_swaps)==0:
                            print("Not Possible")
                            return "failed"
                        else:
                            scorenow=score
                            for xx in range(0,len(av_swaps)):
                                x=first_day[j].copy()
                                x[av_swaps[xx]],x[ind[z]]=x[ind[z]],x[av_swaps[xx]]
                                first_day[j]=x
                                try:
                                    score,ind=fitness(first_day[i],first_day[j])
                                    if score>scorenow:
                                        break
                                except:
                                    return "failed"
                            break
            for k in range(0,len(first_day[i])):
                try:
                    perm_assignemnt[first_day[i][k]].append(k)
                except:
                    perm_assignemnt[first_day[i][k]]=[k]
        final_timetable.append(first_day)
    print(final_timetable)
x=final_schedule()
print(x)
while x=="failed":
    x=final_schedule()
    print(x)