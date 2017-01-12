import os,sys
from os.path import join
from Common_Functions import *


source = "truc"
arg1=111
arg2=333
arg3=222
ra=444
dec=555

open("try.txt",'w').write('<?xml version="1.0" standalone="no"?>'+"\n"+\
                          '<source_library title="source library">'+"\n"+\
                          "\t"+'<source name='+source+' type=PointSource>'+"\n"+\
                            "\t"+"\t"+'<spectrum type="LogParabola">'+"\n"+\
                            "\t"+"\t"+"\t"+'<parameter name="norm"   scale="1e-16" value="'+str(arg1)+'"  min="1e-07" max="1000.0" free="1"/>'+"\n"+\
                                      "\t"+"\t"+"\t"+ '<parameter name="alpha"       scale="-1"    value="'+str(arg2)+'" min="0.0"   max="+5.0"   free="1"/>'+"\n"+\
                                      "\t"+"\t"+"\t"+'<parameter name="beta" scale="1e6"   value="'+str(arg3)+'"  min="0.01"  max="1000.0" free="0"/>'+"\n"+\
                                      "\t"+"\t"+"\t"+'<parameter name="Eb"    scale="1e6"   value="1.0"     min="0.01"  max="1000.0" free="0"/>'+"\n"+\
                            "\t"+"\t"+'</spectrum>'+"\n"+\
                            "\t"+"\t"+'<spatialModel type="SkyDirFunction">'+"\n"+\
                                        "\t"+"\t"+"\t"+'<parameter name="RA"  scale="1.0" value='+str(ra)+' min="-360" max="360" free="0"/>'+"\n"+\
                                        "\t"+"\t"+"\t"+'<parameter name="DEC" scale="1.0" value='+str(dec)+' min="-90"  max="90"  free="0"/>'+"\n"+\
                            "\t"+"\t"+'</spatialModel>'+"\n"+\
                            "\t"+'</source>'+"\n"
                          "\t"+'<source name="CTABackgroundModel" type="CTAIrfBackground" instrument="CTA">'+"\n"+\
                          "\t"+"\t"+'<spectrum type="PowerLaw">'+"\n"+\
                          "\t"+"\t"+"\t"+'<parameter name="Prefactor"   scale="1.0"  value="1.0"  min="1e-3" max="1e+3"   free="1"/>'+"\n"+\
                          "\t"+"\t"+"\t"+'<parameter name="Index"       scale="1.0"  value="0.0"  min="-5.0" max="+5.0"   free="1"/>'+"\n"+\
                          "\t"+"\t"+"\t"+'<parameter name="PivotEnergy" scale="1e6"  value="1.0"  min="0.01" max="1000.0" free="0"/>'+"\n"+\
                          "\t"+"\t"+'</spectrum>'+"\n"+\
                          "\t"+'</source>'+"\n"+\
                          '</source_library>')
