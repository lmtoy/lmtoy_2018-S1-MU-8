#! /usr/bin/env python
#
#   script generator for project="2018-S1-MU-8"
#
#  NGC5194 (M51) :  5 fields, 99 obsnum's
#  NGC628        :  1 field, 13 obsnum's
#
# e.g.       lmtinfo.py grep S1-MU-8 Map | awk '{print $4}' | sort uniq -c
#1     24 NGC5194                115.2712    
#2     29 NGC5194-central         88.6318    
#3     23 NGC5194_north           88.6318    
#4     23 NGC5194_south           88.6318    
#5      1 NGC5194-HCN-central     88.6318    

#  RA,DEC of most fields is:    202.469625  47.195172 (on0,on2,on3,on4,on5)
#         on 13-2020-02-13 is:  202.469583  47.195278  = 0.10" in RA and 0.38" in dec, so ignore ($on1)

#
# 90995 was the first doppler clean data (HCN)
#
import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy + '/lmtoy')
    import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)
    
project="2018-S1-MU-8"  


#        obsnums per source (make it negative if not added to the final combination)
on = {}

on['NGC5194-CO']  = [ 88874,-88882, 88967, 88971,                                 #  jan 15, 16 (all data taken in 2020)
                      90648, 90650, 90652, 90654, 90658, 90660, 90664, 90666,     #  feb 13, but wrong ProjectId='2018S1-MU-8'
                      90740, 90744,-90758,                                        #  feb 14
                      90911, 90915,-90947, 90951,                                 #  feb 18
                     -91037, 91041, 91112,                                        #  feb 19, 20 (first doppler clean data)
                     ]

#  HCN has two source names and two PID's , lots of mistakes
on['NGC5194-HCN']  = [ 90995, 90999,                   # NGC5194                   2018-S1-MU-8  - wrong source name
                       88878,                          # NGC5194-HCN-central       2018-S1-MU-8  - wrong source name
                       88990,                          # NGC5194-central           2018-S1-MU-8
                       90139, 90141, 90143, 90149, 
                       90151, 90155, 90157, 90163,
                       90268, 90270, 90274, 90276,
                       90280, 90282, 90286, 90381,
                       90383, 90385, 90389, 90442,
                       90444, 90446, 90450, 90452,
                       90454, 90458, 90460, 90462

                       91328,                          # NGC5194_north             2018-S1-MU-8
                       91336, 91344, 91350, 91356,
                       91362, 91368, 91523, 91534,
                       91579, 91613, 91619, 91661,
                       91669, 91681, 91713, 92215,
                       92223, 92274, 92286, 92294,
                       92351, 92504,

                       91338,                          # NGC5194_south             2018-S1-MU-8
                       91346, 91352, 91358, 91364,
                       91370, 91525, 91536, 91615,
                       91621, 91663, 91671, 91675,
                       91683, 91715, 92219, 92227,
                       92280, 92290, 92300, 92355,
                       92626,
                      ]

on['NGC628'] = [ 86278,                                     # 8-nov
                 88305, 88307, 88311, 88313, 88315,         # 20-dec
                 88501,                                     # 10-jan   (shorter integration?)
                 88649, 88653,                              # 14-jan
                 88801, 88805,                              # 15-jan
                 88915, 88919,                              # 16-jan
                ]

    
# NGC5194-central
# NGC5194-HCN-central
# NGC5194_north
# NGC5194_south
# NGC628




#        common parameters per source on the first dryrun (run1, run2)
pars1 = {}
pars1['NGC5194-CO']  = "dv=250 dw=250 extent=600"
pars1['NGC5194-HCN'] = "dv=250 dw=250 extent=600"
pars1['NGC628']      = "dv=250 dw=250 extent=400"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['NGC5194-CO']  = "pix_list=1,2,3,4,6,7,8,9,10,11,12,13,14,15"
pars2['NGC5194-HCN'] = "pix_list=1,2,3,4,6,7,8,9,10,11,12,13,14,15"
pars2['NGC628']      = "pix_list=1,2,3,4,6,7,8,9,10,11,12,13,14,15"

runs.mk_runs(project, on, pars1, pars2)

