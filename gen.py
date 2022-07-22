import pandas as pd
import matplotlib.pyplot as plt
p = pd.read_csv('usa.csv')
cumilative_cases = p['cases']
cumilative_deaths = p['deaths']
cases = []
deaths = []
cases.append(cumilative_cases[0])
deaths.append(cumilative_deaths[0])
for i in range(1,len(cumilative_cases)):
    cases.append(cumilative_cases[i]-cumilative_cases[i-1])
    deaths.append(cumilative_deaths[i]-cumilative_deaths[i-1])
    cases[-1] = max(0,cases[-1])
    deaths[-1] = max(0,deaths[-1])
d = p['date']
for i in range(0,len(cases)):
    #print(cases[i],d[i])
    if(d[i]=='2020-06-29'):
        print("alpha",i)
    if(d[i]=='2021-07-01'):
        print("delta",i)
    if(d[i]=='2021-11-01'):
        print("omicron",i)

case_7dayavg = []
avg=0
for i in range(0,7):
    case_7dayavg.append(cases[i])
    avg+=cases[i]

for i in range(7,len(cases)):
    avg-=cases[i-7]
    avg+=cases[i]
    case_7dayavg.append(avg//7)
plt.plot(case_7dayavg[200:400],label='alpha')
leg = plt.legend(loc='upper center')
plt.show()
plt.plot(case_7dayavg[527:650],label='delta')
leg = plt.legend(loc='upper center')
plt.show()
plt.plot(case_7dayavg[650:850],label='omicron')
leg = plt.legend(loc='upper center')
plt.show()
