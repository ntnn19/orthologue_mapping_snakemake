python -c 'import os; os.makedirs("results/inparanoid/set1",exist_ok=True)' && snakemake \
-c24 --use-singularity --singularity-args \
'-B $(pwd)/config/input/inparanoid/set1:/input/ -B $(pwd)/results/inparanoid/set1:/output/' \
--config set=set1 -p -w 60 --rerun-trigger mtime  --sdm conda apptainer
