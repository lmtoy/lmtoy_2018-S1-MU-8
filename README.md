# 2018-S1-MU-8

This project observed NGC5194 (M51) in CO and HCN. Results from these data were published on
arXiv (accepted for publication in ApJ on April 15, 2022) - [Heyer et. al 2022]
See https://arxiv.org/abs/2204.xxxxx

The data produced in the paper were processed with the very first "unnamed" version
of the pipeline: lmtoy_reduce.sh and lmtoy_combine.sh, not this version [lmtoy 0.5 - spring 2022].

NOTE: A few obsnums are by accident in **2018S1-MU-8**.

## OBSNUM

A total of 99 science obsnum's were taken, 77 in the HCN line (88.6 GHz) and 22 in the CO line (115.3 GHz).
The data were taken in a campaign between 15-jan-2020 and 13-mar-2020, the day of the COVID shutdown.
Some more detailed descriptions are in the file **mk_runs**.


## LMTOY Data Reduction

There are two ways to run the SLpipeline, both using the $WORK_LMT directory where the root
of the data is.

1. Use the WORK_LMT that came with where **lmtoy** was installed. This will likely require
   permission from the owner

   This is the way it runs on Unity.

2. Set WORK_LMT to a directory here in this directory,  something like

              WORK_LMT=`pwd`

   and no permissions in the $LMTOY tree are needed. The pipeline will then create all
   data products in this directory.

### Creating the run files

A master script **mk_runs** contains all the information on which obsnums are good,
which beams are good, etc.  You always will need to re-run this script to create the
SLpipeline *run* files. The script also uses the **OBSNUM.args** files, where
arguments specific to this obsnum can be stored. These files should be edited by
a user to create a new "final" dataset. Any optional post-processing after the
pipeline will not be described here (but is recommended?).

This command creates the run files (it uses the **mk_runs** scripts):

      make runs
	  
in this case just **m51.run1** and **m51.run2**

### Running the pipeline


On SLURM this is the way:

      sbatch_lmtoy m51.run1
      # wait for it to finish
      sbatch_lmtoy m51.run2

whereas on Gnu Parallel :

      parallel --jobs 16 m51.run1
      parallel --jobs 16 m51.run2

can be submitted in a shell as the seond one will wait until the first one has finished
all pipeline calls. On "lma" this takes about 30 minutes to process all single obsnums
(run1) and a few combination maps (run2)

If you have no good parallel/batch processing available, the slow and trusted way is:

      bash m51.run1
      bash m51.run2


### Alternate ProjectId's

For the M51 project by accident the ProjectId during one night (2020-02-13, see **lmtinfo.log**)
was given the wrong name. In addition one pointing observation was stored under
2018S1SEQUOIACommissioning.

It may in fact be diserable to add certain pointing observations to the dataset, to confirm
that pointing was optimal. most (all?) osbervations have (or should have) a regular pointing done
before, maybe during, and after an observation. In theory one could use a cross-correlatoin
technique to convince oneselves that the data are safe to stack.  *we will be looking into this*


## Files:


Description of the file that should be in this directory


      do_MU-8p        the original messy script that was used for testing
      lmtinfo.log     logfile from lmtinfo.py on all relevant science observations
      mk_runs         script to make the run files
      m51.run1        created by mk_runs
      m51.run2        created by mk_runs
      lmtinfo.log     output of "lmtinfo.py grep NGC5194"
	  2018-S1-MU-8/   (optional) directory with pipeline results, otherwise in $WORK_LMT
	  2018S1-MU-8/    (optional) directory with pipeline results, otherwise in $WORK_LMT
