import os,sys
from os.path import join
from ctoolsAnalysis.config import get_config,get_default_config
import AlltheSourcesFitLPmodel
import AllSourcesSimulate_Ctools
import AllSourcesFit_Ctools
import matplotlib.pyplot as plt
liste =[]
x = [1,3,10,30,100]
liste.append(x)

with open("Source2.txt") as f:
   for line in f:
        ts = []
        GetSourceInformation(line.split("\t")[0],"")
        print (line.split("\t")[0])

        DoSimulation(line.split("\t")[0],line.split("\t")[5],1)
        tmp=DoFit(line.split("\t")[0],line.split("\t")[5],1)
        ts.append(tmp)
        print ts

        DoSimulation(line.split("\t")[0],line.split("\t")[5],3)
        tmp=DoFit(line.split("\t")[0],line.split("\t")[5],3)
        ts.append(tmp)
        

        DoSimulation(line.split("\t")[0],line.split("\t")[5],10)
        tmp=DoFit(line.split("\t")[0],line.split("\t")[5],10)
        ts.append(tmp)
        

        DoSimulation(line.split("\t")[0],line.split("\t")[5],30)
        tmp=DoFit(line.split("\t")[0],line.split("\t")[5],30)
        ts.append(tmp)
        

        DoSimulation(line.split("\t")[0],line.split("\t")[5],100)
        tmp=DoFit(line.split("\t")[0],line.split("\t")[5],100)
        ts.append(tmp)

        plt.plot(x,ts,label = line.split("\t")[0])
        plt.legend(loc=3)
        plt.ylabel('ts')
        plt.xlabel('Simulation time (h)')
        plt.title("Significativity"+str(source))
        plt.show()


        liste.append(ts)
        

