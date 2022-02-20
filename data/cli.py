import glob
import os
from shutil import copyfile

import click


@click.group()
def core():
    pass


@core.command()
@click.option("--all", type=bool, default=True, help="Import all trades?")
def upload(all):
    from upload_to_portfolio_manager import execute

    import_all: bool = all
    execute(import_all)


@core.command()
def copy():
    csv_files = []
    for file in glob.glob("*.csv"):
        csv_files.append(file)

    for file in csv_files:
        print(f"Deleting = {file}")
        os.remove(file)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    lsc_data_path = dir_path + "/../../finx-ib-reports/data/*trades.csv"

    for file in glob.glob(lsc_data_path):
        # hack to only copy [0-9]_trades.csv files
        if "close" in file:
            continue

        print(f"Copying {file}")
        fn = file.split("/")[-1]
        dest = f"{dir_path}/{fn}"
        copyfile(file, dest)


if __name__ == "__main__":
    core()
