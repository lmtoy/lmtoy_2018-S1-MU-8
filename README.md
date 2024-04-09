# 2018-S1-MU-8

This project observed NGC5194 (M51) in CO and HCN. Results from these data were published in
ApJ on April 15, 2022) - [Heyer et. al 2022]
See https://ui.adsabs.harvard.edu/abs/2011ApJS..193...19K

The data produced for the paper were processed with the very first version
of the pipeline (at the time named lmtoy_reduce.sh and lmtoy_combine.sh).
The purpose of these scripts is not to reproduce the exact data presented in the paper, but
to show a path to reproduce them, and provide a template for other projects.

![Figure 1 from paper](m51.png "Figure 1 from paper")

## OBSNUM

A total of 99 science obsnum's were taken, 77 in the HCN line (88.6 GHz) and 22 in the CO line (115.3 GHz).
The data were taken in a nine week campaign between 15-jan-2020 and 13-mar-2020, the day of the COVID shutdown!
Each observation covered (most of) the galaxy in about 20 minutes of integration time in an OTF style.

Most obsnums are in **2018-S1-MU-8**, but by accident a few are in **2018S1-MU-8**. We fixed the **lmtinfo.py**
tool to sanitize the name, a symlink might also work, but has its own issues.
More detailed descriptions are in the file **mk_runs.py**.

All data prior to 19-feb-2020 suffered from a hardware bug that causes bimodel or trimoal RMS variations. High
values will need to be clipped, and causes about 10-20% of the data to be flagged. The last bad obsnum in this project was
90951, and 90995 was the first good one.

Data views should be available in http://taps.lmtgtm.org/lmtslr/2018-S1-MU-8/README.html

The paper quotes a main beam efficiency of 0.65, and RMS (in main beam scale) of 28 mK for CO and 8 mK for HCN, 
in 5 km/s channels. 

In the earlier reduction, HCN was taken with 7" pixel (16.1" beam), and the CO data with 5.5" pixel (12.65" beam).
The correct beam for HCN should have been 10.6"

### Alternate ProjectId's

For the M51 project by accident the ProjectId during one night (2020-02-13, see **lmtinfo.log**)
was given the wrong name. In addition one pointing observation was stored under
2018S1SEQUOIACommissioning.

It may in fact be diserable to add certain pointing observations to the dataset, to confirm
that pointing was optimal. most (all?) osbervations have (or should have) a regular pointing done
before, maybe during, and after an observation. In theory one could use a cross-correlatoin
technique to convince oneselves that the data are safe to stack.  *we will be looking into this*

The lmtinfo.py program now patched the wrong PID, so it will appear ok now (fixed 2023)

# Birdies

Example:

     tab_plot.py NGC5194-central_90270__0.bstats.tab

shows channel 755 is affected. Others have 646 and/or 647 affected, near the edge of our dv/dw selection, and is
less strong.


90282/NGC5194-central_90282__0.bstats.tab   755 756 (smaller, next to it)


90460/NGC5194-central_90460__0.bstats.tab  a lot - crazy

90951/NGC5194_90951__0.bstats.tab   1027..1031 (5 ) - crazy
