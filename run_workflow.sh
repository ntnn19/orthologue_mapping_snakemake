#!/usr/bin/env bash
python -c 'import os; os.makedirs("results_/inparanoid/set1",exist_ok=True)' && snakemake -c24 --use-singularity --singularity-args '-B $(pwd)/input/inparanoid/set1:/input/ -B $(pwd)/results_/inparanoid/set1:/output/' --config set=set1 -p -w 30
python -c 'import os; os.makedirs("results_/inparanoid/set2",exist_ok=True)' && snakemake -c24 --use-singularity --singularity-args '-B $(pwd)/input/inparanoid/set2:/input/ -B $(pwd)/results_/inparanoid/set2:/output/' --config set=set2 -p -w 30
python -c 'import os; os.makedirs("results_/inparanoid/set3",exist_ok=True)' && snakemake -c24 --use-singularity --singularity-args '-B $(pwd)/input/inparanoid/set3:/input/ -B $(pwd)/results_/inparanoid/set3:/output/' --config set=set3 -p -w 30    
