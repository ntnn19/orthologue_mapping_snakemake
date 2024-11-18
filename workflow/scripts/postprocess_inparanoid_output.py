import click
@click.command()
@click.argument('inparanoid_output', type=click.Path(exists=True), required=True)
@click.argument('output', type=click.Path(), required=True)
def main(inparanoid_output,output):
    inparanoid_df=pd.read_csv(inparanoid_output,header=None ,sep="\t")
    inparanoid_df.columns = ['group', 'bitscore','source','iInparalog_score','id']
    inparanoid_df_piv = inparanoid_df.pivot(index='group', columns='source')
    species =  inparanoid_df.source.unique()

    s1 = species[0]
    s2 = species[1]
    groups2 = inparanoid_df_piv.groupby(("id",s2))
    groups1 = inparanoid_df_piv.groupby(("id",s1))

    groups1_of_size_1 = groups1.filter(lambda x: len(x) == 1)
    groups2_of_size_1 = groups2.filter(lambda x: len(x) == 1)

    # 1:1
    df1=groups1_of_size_1.merge(groups2_of_size_1)
    df1['orthotype'] = '1:1'

    # 1:m
    groups1_of_size_above_1 = groups1.filter(lambda x: len(x) > 1)
    df2=groups1_of_size_above_1.merge(groups2_of_size_1)
    df2['orthotype'] = '1:m'

    # print(df2.orthotype.value_counts())
    # n:1
    groups2_of_size_above_1 = groups2.filter(lambda x: len(x) > 1)
    df3=groups2_of_size_above_1.merge(groups1_of_size_1)
    df3['orthotype'] = 'n:1'

    # m:n
    t = pd.concat([df1, df2, df3])
    many_to_many_rows = inparanoid_df_piv[~inparanoid_df_piv.isin(t.to_dict('list')).all(axis=1)]
    final_df = pd.concat([t,many_to_many_rows])
    final_df['orthotype'] = final_df['orthotype'].fillna("n:m")

        # final_df =
    # if not os.path.exists(out):
    final_df.to_csv(output,index=False)


    print(final_df
          ['orthotype'].value_counts())
    return final_df




if __name__ == '__main__':
    import yaml
    import os
    import pandas as pd
    from pathlib import Path
    import pdb
    main()
