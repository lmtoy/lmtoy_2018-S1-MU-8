# 2018-S1-MU-8

This project observed NGC5194 (M51) in CO and HCN. It was published in
arXiv
(accepted for publication in ApJ on April 15, 2022)

The data produced in the paper were processed with the very first "unnamed" version
of the pipeline: lmtoy_reduce.sh and lmtoy_combine.sh.

NOTE: A few obsnums are in 2018S1-MU-8 - this is unusual, but we have to deal with it.


## Running the pipeline

There are two ways to run the pipeline, both using the $WORK_LMT directory where the root
of the data is.

1. Use the WORK_LMT that came with where **lmtoy** was installed. This will likely require
   permission from the owner

2. Set WORK_LMT to a directory here in this directory,  something like

              WORK_LMT=`pwd`

   and no permissions in the $LMTOY tree are needed.

On SLURM this is the way:

      sbatch_lmtoy m51.run1
      # wait for it to finish
      sbatch_lmtoy m51.run2

whereas on Gnu Parallel :

      parallel --jobs 16 m51.run1
      parallel --jobs 16 m51.run2

can be submitted in a shell as the first one will not finish until all jobs are done.


## Files:

The run1 and run2 files are kept separate, because each by themselved can be run in parallel
(e.g. using SLURM or Gnu Parallel), but run2 needs to wait for run1 to finish before it can
start.


      do_MU-8p - for the record, this is the original script that was used for testing
      
      
