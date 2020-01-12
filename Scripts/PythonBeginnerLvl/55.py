# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:30:14 2019

@author: Mateusz.Jaworski
"""

q='THE EYES'

print(q)
print(q[0],q[1],q[2],q[3],q[4],q[5],q[6])

z='a gentelman'
print(z[3],z[6],z[7],z[2],z[0],z[4],z[5],z[1],z[8:])

x='THE MORSE CODE'

print(x[1:3],x[6],x[8],x[3],x[9:11],x[4],x[2],x[3],x[12],x[11],x[0],x[7])

print(x[1:3],x[6],x[8],x[3],x[10:12],x[4],x[13],x[9],x[12],x[5],x[0],x[7])

line='Program "Kropka nad i" nadamy o: 22:00'

time=line[line.find(":")+2:]

print(time)

tmp=line[line.find('"')+1:]

print(tmp)

title=tmp[:tmp.find('"')]

print(title,time)