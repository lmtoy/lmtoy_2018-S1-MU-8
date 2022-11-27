#


PID = 2018-S1-MU-8 

help:
	@echo WORK_LMT=$(WORK_LMT)
	@echo PID=$(PID)
	@echo Targets here:
	@echo "   runs      - make the run1/run2/... files"
	@echo "   summary   - update the project summary index"
	@echo "               https://taps.lmtgtm.org/lmtslr/$(PID)"


runs:
	./mk_runs.py

summary:
	@for p in $(PID); do \
	(echo $$p; cd $(WORK_LMT)/$$p; mk_summary1.sh > README.html); \
	done
	@echo Make sure comments.txt and index.html are symlinked
