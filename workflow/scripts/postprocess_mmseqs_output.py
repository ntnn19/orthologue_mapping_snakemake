import click
@click.command()
@click.argument('mmseqs_output', type=click.Path(exists=True), required=True)
@click.argument('output', type=click.Path(), required=True)
def main(mmseqs_output,output):
    mmseqs_output_piv=pd.read_csv(mmseqs_output,header=None ,sep="\t")
    mmseqs_output_piv.columns = 'query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits,qcov,tcov'.split(",")

    species = mmseqs_output_piv.columns.tolist()[:2]

    s1 = species[0]
    s2 = species[1]
    groups2 = mmseqs_output_piv.groupby(s2)
    groups1 = mmseqs_output_piv.groupby(s1)

    groups1_of_size_1 = groups1.filter(lambda x: len(x) == 1)
    groups2_of_size_1 = groups2.filter(lambda x: len(x) == 1)

    # 1:1
    df1=groups1_of_size_1.merge(groups2_of_size_1)
    df1['orthotype'] = '1:1'

    # 1:m
    groups1_of_size_above_1 = groups1.filter(lambda x: len(x) > 1)
    df2=groups1_of_size_above_1.merge(groups2_of_size_1)
    df2['orthotype'] = '1:m'

    # n:1
    groups2_of_size_above_1 = groups2.filter(lambda x: len(x) > 1)
    df3=groups2_of_size_above_1.merge(groups1_of_size_1)
    df3['orthotype'] = 'n:1'

    # m:n
    t = pd.concat([df1, df2, df3])
    many_to_many_rows = mmseqs_output_piv[~mmseqs_output_piv.isin(t.to_dict('list')).all(axis=1)]
    final_df = pd.concat([t,many_to_many_rows])
    final_df['orthotype'] = final_df['orthotype'].fillna("n:m")

    final_df.to_csv(output,index=False)


    return final_df




if __name__ == '__main__':
    import yaml
    import os
    import pandas as pd
    from pathlib import Path
    import pdb
    main()
