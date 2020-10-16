import pathlib
import pandas as pd
import geopandas as gpd

keep_cols = [
    "FULL_ADDRESS",
    "ADDRESS_CITY",
    "STATE_NAME",
    "ADDRESS_ZIP",
    "ADDRESS_COUNTY",
    "LATITUDE",
    "LONGITUDE",
]

# data_dir = pathlib.Path(__file__).parent.parent.joinpath("data", "processed")
data_dir = pathlib.Path().cwd().parent.joinpath("data", "processed")
# print(data_dir)
source_fname = "County_Address_Points_IGIO_IN.json"
# source_fname = "subset_address_points.json"
source_fpath = data_dir.joinpath(source_fname)

saveas_fpath = data_dir.joinpath(source_fpath.stem + ".parquet")
# print(source_fpath.exists())
# print(saveas_fpath.exists())

# raise SystemExit
gpd.read_file(source_fpath)[keep_cols].to_parquet(str(saveas_fpath))