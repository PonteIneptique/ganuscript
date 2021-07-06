#!/bin/sh

for testfile in ./prediction/htr/test-sets/test-microfilm-*.txt; \
	do for model in ./models/htr/*.mlmodel; \
		do echo "TESTFILE:$testfile" && \
			echo "MODEL:$model" && \
			ketos test -u NFC --threads 10 -e $testfile -f alto -m $model;\
		done;
	done
