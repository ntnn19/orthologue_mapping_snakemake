#!/usr/bin/env bash
#inparanoid
python -c 'import os; os.makedirs("results/inparanoid/set1",exist_ok=True)' && snakemake results/inparanoid/set1/SQLtable.Reference_proteome_Ae_aegypti_LVP_AGWG_UP000008820_7159.fasta-Reference_proteome_D_melanogaster_UP000000803_7227.fasta.orthotype.csv -c24 --use-singularity --singularity-args '-B $(pwd)/input/inparanoid/set1:/input/ -B $(pwd)/results/inparanoid/set1:/output/'
python -c 'import os; os.makedirs("results/inparanoid/set2",exist_ok=True)' && snakemake results/inparanoid/set2/SQLtable.Reference_proteome_Ae_aegypti_LVP_AGWG_UP000008820_7159.fasta-Reference_proteome_Mouse_UP000000589_10090.fasta.orthotype.csv -c24 --use-singularity --singularity-args '-B $(pwd)/input/inparanoid/set2:/input/ -B $(pwd)/results/inparanoid/set2:/output/'
python -c 'import os; os.makedirs("results/inparanoid/set3",exist_ok=True)' && snakemake results/inparanoid/set3/SQLtable.Reference_proteome_Ae_aegypti_LVP_AGWG_UP000008820_7159.fasta-Reference_proteome_Human_uniprot_9606_reviewed_canonical_isoforms_191008.fasta.orthotype.csv -c24 --use-singularity --singularity-args '-B $(pwd)/input/inparanoid/set3:/input/ -B $(pwd)/results/inparanoid/set3:/output/'
#mmseqs
snakemake -c24 --use-singularity
