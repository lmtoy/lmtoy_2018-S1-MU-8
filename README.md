# 2018-S1-MU-8

This project observed NGC5194 (M51) in CO and HCN. It was published in
arXiv
(accepted for publication in ApJ on April 15, 2022) - [Heyer et. al 2022]

The data produced in the paper were processed with the very first "unnamed" version
of the pipeline: lmtoy_reduce.sh and lmtoy_combine.sh.

NOTE: A few obsnums are in **2018S1-MU-8** - this is unusual, but we have to deal with it.


## LMTOY Data Reduction

There are two ways to run the pipeline, both using the $WORK_LMT directory where the root
of the data is.

1. Use the WORK_LMT that came with where **lmtoy** was installed. This will likely require
   permission from the owner

   This is likely the way it will run on Unity.

2. Set WORK_LMT to a directory here in this directory,  something like

              WORK_LMT=`pwd`

   and no permissions in the $LMTOY tree are needed. The pipeline will then create all
   data products in this directory.

### Creating the run files

A master script **mk_runs** contains all the information on which obsnums are good,
which beams are good, etc.  You always will need to re-run this script


### Running the pipeline


On SLURM this is the way:

      sbatch_lmtoy m51.run1
      # wait for it to finish
      sbatch_lmtoy m51.run2

whereas on Gnu Parallel :

      parallel --jobs 16 m51.run1
      parallel --jobs 16 m51.run2

can be submitted in a shell as the first one will not finish until all jobs are done.

If you have no good parallel/batch processing available, the slow and trusted way is:

      bash m51.run1
      bash m51.run2


### Alternate ProjectId's

For the M51 project by accident the ProjectId during one night (2020-02-13, see **lmtinfo.log**)
was given the wrong ProjectId. In addition one pointing observation was stored under
2018S1SEQUOIACommissioning.

In addition, it may be diserable to add certain pointing observations to the dataset, to confirm
that pointing was optimal. most (all?) osbervations have (or should have) a regular pointing done
before, maybe during, and after an observation. In theory one could use a cross-correlatoin
technique to convince oneselves that the data are safe to stack.


## Files:

The run1 and run2 files are kept separate, because each by themselved can be run in parallel
(e.g. using SLURM or Gnu Parallel), but run2 needs to wait for run1 to finish before it can
start.


      do_MU-8p      the original messy script that was used for testing
      lmtinfo.log   logfile from lmtinfo.py on all relevant science observations
      mk_runs       script to make the run files
      m51.run1      Created by mk_runs
      m51.run2      Created by mk_runs
      
