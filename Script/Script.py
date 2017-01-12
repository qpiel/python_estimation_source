import os,sys
from os.path import join
from ctoolsAnalysis.config import get_config,get_default_config
import AlltheSourceFitLPmodel
import AllSourcesSimulate_Ctools
import AllSourcesFit_Ctools
x = []
ts = []
with open("Source2.txt") as f:
   for line in f:
        GetSourceInformation(line.split("\t")[0],"")
        print (line.split("\t")[0])

        DoSimulation(line.split("\t")[0],line.split("\t")[5],1)
        tmp=DoFit(line.split("\t")[0],line.split("\t")[5],1)
        ts.append(tmp)
        x.append(1)

        DoSimulation(line.split("\t")[0],line.split("\t")[5],3)
        tmp=DoFit(line.split("\t")[0],line.split("\t")[5],3)
        ts.append(tmp)
        x.append(3)

        DoSimulation(line.split("\t")[0],line.split("\t")[5],10)
        tmp=DoFit(line.split("\t")[0],line.split("\t")[5],10)
        ts.append(tmp)
        x.append(10)

        DoSimulation(line.split("\t")[0],line.split("\t")[5],30)
        tmp=DoFit(line.split("\t")[0],line.split("\t")[5],30)
        ts.append(tmp)
        x.append(30)

        DoSimulation(line.split("\t")[0],line.split("\t")[5],100)
        tmp=DoFit(line.split("\t")[0],line.split("\t")[5],100)
        ts.append(tmp)
        x.append(100)