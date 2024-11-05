import os.path

import click
@click.command()
@click.argument('working_dir', type=click.Path(exists=True), required=True)
@click.argument('colabfold_weights_dir', type=click.Path(), required=True)
def main(working_dir,colabfold_weights_dir):
# def main(working_dir):
# def main(config_file):
    # DATA_DIR = conf["data_dir"]
    # RESULTS_DIR = conf["output_dir"]
    output_dir= os.path.join(working_dir,'output')
    predictions_dir= os.path.join(output_dir,'predictions')
    reports_dir= os.path.join(output_dir,'reports')
    data_dir= os.path.join(output_dir,'data')
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(predictions_dir, exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)
    print(colabfold_weights_dir)
    os.makedirs(colabfold_weights_dir, exist_ok=True)
    return output_dir,predictions_dir, reports_dir, data_dir





if __name__ == '__main__':
    import yaml
    import os
    from pathlib import Path
    main()
