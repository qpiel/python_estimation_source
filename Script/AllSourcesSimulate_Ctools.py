import os,sys
from os.path import join
import ctools
from ctoolsAnalysis.config import get_config,get_default_config
from ctoolsAnalysis.SimulateSource import CTA_ctools_sim
from Common_Functions import *
import math

Astropy = True
try :
    import Coordinates.CoordHandler as CH
    import Coordinates.CoordUtilities as CU
    from astropy.coordinates import FK5 
except :
    Astropy = False
def DoSimulation(source,area,simutime):
    #define source name. This also allows to have the coordinate if you have astropy
    #source = "AP Librae"
    ra = None
    dec = None
    if Astropy:
        coord = CH.CoordinatesHandler.fromName(source,FK5)
        ra, dec = CU.GetCoordInDegrees(coord)
     
    #default work and out path. Not use if you provide a config file in the command line
    #out =  join(os.getcwd(), "out")
    #work = join(os.getcwd(), "work")
    out = "/Users/gateflorian/Documents/CTAtools/Script/out"
    work = "/Users/gateflorian/Documents/CTAtools/Script/work"
        # setup : Time, Energy and IRFS. Not use if you provide a config file in the command line
    tmin = 0
    #tmax = 3600
    tmaxtmp = simutime*3600
    tmax = int(tmaxtmp)
    print tmax
    irfTime = IrfChoice(simutime)
    emin = 0.2
    emax = 10

    irf = str(area)+"_"+str(irfTime)+"h"
    print irf
    caldb = "prod2"
    #irf = "South_0.5h"

    # Not use if you provide a config file in the command line
    try :#conf file provided
      config_tmp = get_config(sys.argv[1])
      config = MakeconfigFromFile(out,work,source,ra,dec,config_tmp)
    except :
      config = MakeconfigFromDefault(out,work,source,ra,dec)
      config.write(open("simu_"+source.replace(" ","")+"_"+str(simutime)+"h"+".conf", 'w'))

    #creation of the simulation object
    simu = CTA_ctools_sim.fromConfig(config)   

    #set up if there is no config file provided
    if len(sys.argv) == 1 :
      simu.SetTimeRange(tmin,tmax)
      simu.SetEnergyRange(emin,emax)
      simu.SetIRFs(caldb,irf)
    
    simu.config.write(open(work+"/simu_"+source.replace(" ","")+"_"+str(simutime)+"h"+".conf", 'w'))
    # run 
    simu.run_sim(prefix = source.replace(" ","")+"_"+str(simutime)+"h" ,nsim = 1, write=True, clobber = True)
    simu.Print()
    return

    


def IrfChoice(simutime):
    attempt1=abs(simutime-0.5)
    attempt2=abs(simutime-5)
    attempt3=abs(simutime-50)
    mini=min(attempt1,attempt2,attempt3)
    if mini==attempt1:
       irfResult=0.5
    elif mini==attempt2:
        irfResult=5
    else:
        irfResult=50

    return irfResult

#DoSimulation("AP Librae","South",0.5)
with open("Source2.txt") as f:
  for line in f:
 ##      print (line.split("\t")[0])
   #     print (line.split("\t")[1])
    #    print (line.split("\t")[2])
     #   print (line.split("\t")[3])
      #  print (line.split("\t")[4])
       # print (line.split("\t")[])
        print line.split("\t")[0]
        #DoSimulation(line.split("\t")[0],line.split("\t")[5],1)
        DoSimulation(line.split("\t")[0],line.split("\t")[5],0.3)
        #DoSimulation(line.split("\t")[0],line.split("\t")[5],10)
        #DoSimulation(line.split("\t")[0],line.split("\t")[5],30)
        #DoSimulation(line.split("\t")[0],line.split("\t")[5],100)