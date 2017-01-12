import os,sys
from os.path import join
import ctools
from ctoolsAnalysis.config import get_config,get_default_config
from ctoolsAnalysis.LikeFit import CTA_ctools_analyser
from Common_Functions import *

Astropy = True
try :
    import Coordinates.CoordHandler as CH
    import Coordinates.CoordUtilities as CU
    from astropy.coordinates import FK5 
except :
    Astropy = False
def DoFit(source,area,simutime):
    #define source name. This also allows to have the coordinate if you have astropy
    #source = "AP Librae"
    
    ra = None
    dec = None
    if Astropy:
        coord = CH.CoordinatesHandler.fromName(source,FK5)
        ra, dec = CU.GetCoordInDegrees(coord)
     

    #default work and out path. Not use if you provide a config file in the command line
    out =  join(os.getcwd(), "out")
    work = join(os.getcwd(), "work")

    # setup : Time, Energy and IRFS. Not use if you provide a config file in the command line
    tmin = 0
    #tmax = 3600
    tmaxtmp=simutime*3600
    tmax = int(tmaxtmp)
    irfTime=IrfChoice(simutime)
    emin = 0.2
    emax = 10
    irf = str(area)+"_"+str(irfTime)+"h"
    caldb = "prod2"
    #irf = "South_0.5h"



    #quentin
    fitsFile = out+"/"+source.replace(" ","")+"_"+str(simutime)+"h"+"_event00001.fits"
    #fitsFile="/Users/gateflorian/Documents/CTAtools/Script/out/Mkn180_event00001.fits"
    #fitsFile = "/Users/gateflorian/Documents/CTAtools/Script/out/table_20161213.fits"

    try:  #conf file provided
        config_tmp = get_config(sys.argv[-1])
        config = MakeconfigFromFile(out,work,source,ra,dec,config_tmp)
        #config["file"]["inobs"] = sys.argv[-2]
        config["file"]["inobs"] = fitsFile
    except:    #Not use if you provide a config file in the command line
        config = MakeconfigFromDefault(out,work,source,ra,dec)
        config["file"]["inobs"] = fitsFile
        #config["file"]["inobs"] = sys.argv[-1]
        config.write(open(work+"/Fit_"+source.replace(" ","")+"_"+str(simutime)+"h"+".conf", 'w'))

    Analyse = CTA_ctools_analyser.fromConfig(config)

    #set up if there is no config file provided
    if len(sys.argv) == 1 :
        Analyse.SetTimeRange(tmin,tmax)
        Analyse.SetEnergyRange(emin,emax)
        Analyse.SetIRFs(caldb,irf)

    Analyse.create_fit(log = True,debug = False)
    Analyse.fit()
    Analyse.PrintResults()

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



#DoFit("AP Librae","South",0.5)
with open("Source2.txt") as f:
  for line in f:
#      print (line.split("\t")[0])
       DoFit(line.split("\t")[0],line.split("\t")[5],0.3)
       #raw_input("Press Enter to terminate.")
       #DoFit(line.split("\t")[0],line.split("\t")[5],3)
       #raw_input("Press Enter to terminate.")
       #DoFit(line.split("\t")[0],line.split("\t")[5],10)
       #DoFit(line.split("\t")[0],line.split("\t")[5],30)
       #DoFit(line.split("\t")[0],line.split("\t")[5],100)
