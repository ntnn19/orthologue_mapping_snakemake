import os.path

import click
@click.command()
@click.argument('inparanoid_output', type=click.Path(exists=True), required=True)
@click.argument('output', type=click.Path(), required=True)
def main(inparanoid_output,output):
    inparanoid_df=pd.read_csv(inparanoid_output,header=None ,sep="\t")
    inparanoid_df.columns = ['group', 'bitscore','source','iInparalog_score','id']

    rows = []
    for i in inparanoid_df.set_index('group').index.unique():
        tmp_rows = []
        tmp = inparanoid_df.set_index('group').loc[i]
        # if tmp.shape[0] > 5:
        source_1_ids = tmp[tmp.source == tmp.source.unique()[0]]
        source_2_ids = tmp[tmp.source == tmp.source.unique()[1]]
        for i in range(source_1_ids.shape[0]):
            for j in range(source_2_ids.shape[0]):
                tmp_rows.append((source_1_ids.iloc[i],source_2_ids.iloc[j]))
        rows.append(tmp_rows)
    print(pd.DataFrame(rows))
    pd.DataFrame(rows).to_csv(output,index=False)




if __name__ == '__main__':
    import yaml
    import os
    import pandas as pd
    from pathlib import Path
    main()
