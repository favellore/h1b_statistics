#!/usr/bin/env python
# coding: utf-8

# In[5]:



# program that constructs a text file from H1B database for Top 10 State and Top 10 Occupation certified for H1B

# Import csv file

file='input/h1b_input.csv'

occupation=[]

for line in open(file):

# We need to split the csv file to read accordingly, the split is done with ';'

    val=line.split(';')
    
#The length of the total csv is more than 41 columns, however we need to restrict data calculations to certain columns to 
# save time. 

    if(len(val)==41):
        
# The problem statement ask for top 10 CERTIFIED H1B State and Top 10 Occupations CERTIFIED
# Hence the variable CERTIFIED is selected which is in column 2.

        if(val[2]=='CERTIFIED'):
        
# Column 22 has the Occupations specified, hence CERTIFIED & OCCUPATION is filtered accordingly.

            x=val[22]           
            y=val[11]
            occupation.append(x)        
x=[]
y=[]
num=0
for f in set(occupation):

# The below code will append the data, so that it adds up cummilative.

    x.append(f)
    y.append(occupation.count(f))
    num+=occupation.count(f)
    
# For getting the ranking order

dat=dict(zip(x,y))
sorted_dat = sorted(dat.items(), key=lambda kv: kv[1])
sorted_dat.reverse() # to get rank ordering 

# Below code will open a text file, by name 'top_10_occupations.txt' with a writing parameter so that we can
# add the result to this file as output accordingly.

occupation=open('output/top_10_occupations.txt','w')  

# The header for TOP OCCUPATION has TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE, which is stored in the file occupation
# Intrun saves in the text file.

#print('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE',file=occupation)

# The below code will have top ten certified application
# we need top 10 with one decimal percentage.

for x in range(1,11,1):
    n=sorted_dat[x][0]
    m=sorted_dat[x][1]
    print(n,m,'{:.1%}'.format(m/num),sep=';'+'output/top_10_occupations.txt')
    
# The code below closes the text file by writing the above output in the text file 'top_10_state.txt' accordingly

occupation.close()

# BELOW CODE IS TO CALCULATE TOP 10 States

state=[]
for line in open(file):
    
# We need to split the csv file to read accordingly, the split is done with ';'
    
    val=line.split(';')
    
#The length of the total csv is more than 41 columns, however we need to restrict data calculations to certain columns to 
# save time. 

    if(len(val)==41):
        
# The problem statement ask for top 10 CERTIFIED H1B State and Top 10 Occupations CERTIFIED
# Hence the variable CERTIFIED is selected which is in column 2.

        if(val[2]=='CERTIFIED'):
        
# Column 11 has the Occupations specified, hence CERTIFIED & OCCUPATION is filtered accordingly.

            a=val[11]              # col-11 is the State col
            b=val[11]
            state.append(a) 
a=[]
b=[]
num=0

# The below code will append the data, so that it adds up cummilative.

for s in set(state):
    a.append(s)
    b.append(state.count(s))
    num+=state.count(s)
    
# For getting the ranking order

dats=dict(zip(a,b))
sorted_dats = sorted(dats.items(), key=lambda kvs: kvs[1])
sorted_dats.reverse() # to get rank ordering 

# Below code will open a text file, by name 'top_10_state.txt' with a writing parameter so that we can
# add the result to this file as output accordingly.

state=open('output/top_10_states.txt','w')    

# The header for TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE, which is stored in the file occupation
# Intrun saves in the text file.

#print('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE',file=state)

# The below code will have top ten certified application
# we need top 10 with one decimal percentage.

for a in range(1,11,1):
    o=sorted_dats[a][0]
    p=sorted_dats[a][1]
    print(o,p,'{:.1%}'.format(p/num),sep=';'+'output/top_10_states.txt')
    
# The code below closes the text file by writing the above output in the text file 'top_10_state.txt' accordingly
    
state.close()


# In[ ]:




