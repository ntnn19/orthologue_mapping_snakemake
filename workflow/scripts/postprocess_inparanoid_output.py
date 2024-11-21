import click
@click.command()
@click.argument('inparanoid_output', type=click.Path(exists=True), required=True)
@click.argument('output', type=click.Path(), required=True)
def main(inparanoid_output,output):
    inparanoid_df=pd.read_csv(inparanoid_output,header=None ,sep="\t")
    inparanoid_df.columns = ['group', 'bitscore','source','iInparalog_score','id']
    print(inparanoid_df)       
    inparanoid_df_piv = inparanoid_df.reset_index().pivot(index=['index'],columns='source',values=['bitscore','iInparalog_score','id','group'])
#    inparanoid_df_piv = inparanoid_df.reset_index().pivot(index='group',columns='source',values=['bitscore','iInparalog_score','id','group'])

#    inparanoid_df_piv = inparanoid_df.pivot(columns='source')
    print(inparanoid_df_piv)
    bitscore = inparanoid_df_piv['bitscore'].bfill(axis=1).infer_objects(copy=False).iloc[:, 0]
    bitscore.name = "bitscore"

    iInparalog_score = inparanoid_df_piv['iInparalog_score'].bfill(axis=1).infer_objects(copy=False).iloc[:, 0]
    iInparalog_score.name = "iInparalog_score"

    group = inparanoid_df_piv['group'].bfill(axis=1).infer_objects(copy=False).iloc[:, 0]
    group.name = "group"
 
    species =  inparanoid_df.source.unique()

    s1 = species[0]
    s2 = species[1]
    id1 = inparanoid_df_piv[("id",s1)].ffill()
    id1.name = "id1"
    id2 = inparanoid_df_piv[("id",s2)].bfill()
    id2.name = "id2"
    inparanoid_df_piv = pd.concat([bitscore,iInparalog_score,id1,id2,group],axis=1).reset_index().drop('index',axis=1).drop_duplicates()


    groups2 = inparanoid_df_piv.groupby("id2")
    groups1 = inparanoid_df_piv.groupby("id1")

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
    final_df['uniprot_id_1'] = final_df.id1.str.split("|").str[1]
    final_df['uniprot_id_2'] = final_df.id2.str.split("|").str[1]
    final_df['species_1'] = final_df.id1.str.split("_").str[-1]
    final_df['species_2'] = final_df.id2.str.split("_").str[-1]

    print(final_df['orthotype'].value_counts())
        # final_df =
    # if not os.path.exists(out):
    final_df.to_csv(output,index=False)


    return final_df




if __name__ == '__main__':
    import yaml
    import os
    import pandas as pd
    from pathlib import Path
    import pdb
    main()
