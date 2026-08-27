import click
@click.command()
@click.argument('inparanoid_output', type=click.Path(exists=True), required=True)
@click.argument('mmseqs_output', type=click.Path(), required=True)
@click.option('--output', type=click.Path(), default='results/get_mmseqs_not_in_inparanoid/output.csv',required=True)
def main(inparanoid_output,mmseqs_output,output):
    inparanoid_df=pd.read_csv(inparanoid_output)
    mmseqs_df=pd.read_csv(mmseqs_output)
    os.makedirs(os.path.dirname(output),exist_ok=True)
    # Drop queriers & targets from mmseqs output if they already appear in inparanoid output
    mmseqs_unique = mmseqs_df[~(mmseqs_df[['query','target']].isin(inparanoid_df[['uniprot_id_1','uniprot_id_2']].values.flatten().tolist()))][['query','target']]
    filtered_mmseqs_df = mmseqs_df.loc[mmseqs_unique.dropna().index]
    filtered_mmseqs_df.to_csv(output,index=False)




if __name__ == '__main__':
    import yaml
    import os
    import pandas as pd
    from pathlib import Path
    main()
