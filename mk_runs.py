#! /usr/bin/env python
#
#   script generator for project="2018-S1-MU-8" (but with a shadow  2018S1-MU-8"  projectId)
#
#  NGC5194 (M51) :  5 fields, 99 obsnum's  - in CO and HCN
#  NGC628        :  1 field, 13 obsnum's
#
#  RA,DEC of most fields is:    202.469625  47.195172 (on0,on2,on3,on4,on5)
#         on 13-2020-02-13 is:  202.469583  47.195278  = 0.10" in RA and 0.38" in dec, so ignore ($on1)
#
#
# 90995 was the first doppler clean data (HCN)
#
# the 600" CO field takes about 2:50 hours per obsnum on unity, but could be made a bit smaller
#
import os
import sys
from lmtoy import runs


#   notice a shadow project is 2018S1-MU-8 that needs a symlink to 2018-S1-MU-8
project="2018-S1-MU-8"  

#        obsnums per source (make it negative if not added to the final combination)
on = {}

                    #   18 of the 22 here are good (4 have a focus issue)
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
                       90139, 90141,-90143, 90149, 
                       90151, 90155, 90157, 90163,
                       90268, 90270, 90274, 90276,
                       90280, 90282, 90286, 90381,
                       90383, 90385, 90389, 90442,
                       90444, 90446, 90450, 90452,
                       90454, 90458, 90460, 90462,
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
                -88501,                                     # 10-jan   crazy sky coverage
                 88649, 88653,                              # 14-jan
                 88801, 88805,                              # 15-jan
                 88915, 88919,                              # 16-jan
                -80101,-80099,-80097,-80093,-80091,         # 20-nov-2018  in 2018S1SEQUOIACommissioning
                -80089,-80087,-80045,-80043,                # adding these make CO signal disappear
                ]

    
#        common parameters per source on the first run (run1a, run2a)
pars1 = {}
pars1['NGC5194-CO']  = "dv=250 dw=250 extent=600"
pars1['NGC5194-HCN'] = "dv=250 dw=250 extent=600"      # needs a birdie fix
pars1['NGC628']      = "dv=100 dw=150 extent=240"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['NGC5194-CO']  = "pix_list=1,2,3,4,6,7,8,9,10,11,12,13,14,15"
pars2['NGC5194-HCN'] = ""     # see comments.txt
pars2['NGC628']      = ""     # see comments.txt

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)

