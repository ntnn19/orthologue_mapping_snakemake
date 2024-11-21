import click
@click.command()
@click.argument('inparanoid_output', type=click.Path(exists=True), required=True)
@click.argument('mmseqs_output', type=click.Path(), required=True)
@click.option('--outdir', type=click.Path(), default='results/mmseqs_easy_rbh',required=True)
def main(inparanoid_output,mmseqs_output,outdir):
    inparanoid_df=pd.read_csv(inparanoid_output)
    mmseqs_df=pd.read_csv(mmseqs_output)
    os.makedirs(outdir,exist_ok=True)
    output=os.path.join(outdir,f"{os.path.splitext(os.path.basename(mmseqs_output))[0]}.not_in_inparanoid.csv")
    # Drop queriers & targets from mmseqs output if they already appear in inparanoid output
    mmseqs_unique = mmseqs_df[~(mmseqs_df[['query','target']].isin(inparanoid_df[['uniprot_id_1','uniprot_id_2']].values.flatten().tolist()))][['query','target']]
    mmseqs_non_unique = mmseqs_df[(mmseqs_df[['query','target']].isin(inparanoid_df[['uniprot_id_1','uniprot_id_2']].values.flatten().tolist()))][['query','target']]
    filtered_mmseqs_df = mmseqs_df.loc[mmseqs_unique.dropna().index]
    filtered_mmseqs_df.to_csv(output,index=False)
#
#
#    return final_df




if __name__ == '__main__':
    import yaml
    import os
    import pandas as pd
    from pathlib import Path
    import pdb
    main()
