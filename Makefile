#


RUN1 = m51.run1
RUN2 = m51.run2

help:
	@echo There is no help here


$(RUN1):	mk_runs
	./mk_runs

$(RUN2):	mk_runs
	./mk_runs

run1:
	@echo "Submit run1 using any of these methods:"
	@echo "    sbatch_lmtoy.sh $(RUN1)"
	@echo "    parallel --jobs 16 < $(RUN1)"
	@echo "    bash $(RUN1)"
	@echo "when this is done, run2 can be started"
run2:
	@echo submit run2 using any of these methods:
	@echo "    sbatch_lmtoy.sh $(RUN2)"
	@echo "    parallel --jobs 16 < $(RUN2)"
	@echo "    bash $(RUN2)"

