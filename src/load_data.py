import pandas as pd
import pathlib

DATA_DIR = pathlib.Path(__file__).parent.parent.joinpath("data", "raw")

PARCEL_DATE_COLS = (("DateToOwner", r"%m/%d/%Y"), ("AppraisalDate", r"%Y-%m-%d"))

PARCEL_FILE_COLS = [
    (25, 0, "ParcelNum", str),
    (25, 1, "LocalParcelNum", str),
    (4, 2, "TownshipNum", int),
    (3, 3, "LocalTaxDistrictNum", str),
    (3, 4, "StateTaxDistrictNum", int),
    (8, 5, "SectionPlat", str),
    (25, 6, "RoutingNum", str),
    (60, 7, "PropAddress", str),
    (30, 8, "PropCity", str),
    (10, 9, "PropZIP", str),
    (3, 10, "PropClass", str),
    (12, 11, "NeighID", str),
    (5, 12, "NeighFactor", float),
    (5, 13, "AdjFactorLand", float),
    (5, 14, "AdjFactorImprovements", float),
    (80, 15, "Owner", str),
    (60, 16, "OwnerAddress", str),
    (30, 17, "OwnerCity", str),
    (30, 18, "OwnerState", str),
    (10, 19, "OwnerPostal", str),
    (3, 20, "OwnerCountry", str),
    (10, 21, "DateToOwner", None),
    (1, 22, "Level", str),
    (1, 23, "High", str),
    (1, 24, "Low", str),
    (1, 25, "Rolling", str),
    (1, 26, "Swampy", str),
    (1, 27, "Water", str),
    (1, 28, "Sewer", str),
    (1, 29, "Gas", str),
    (1, 30, "Electricity", str),
    (1, 31, "StreetCode", str),
    (1, 32, "Sidewalk", str),
    (1, 33, "Alley", str),
    (1, 34, "NeighType", str),
    (3, 35, "WaterPropType", str),
    (5, 36, "Zoning", str),
    (1, 37, "FloodHazard", str),
    (12, 38, "ValueLand", float),
    (12, 39, "ValueImprove", float),
    (12, 40, "ValueTotal", float),
    (12, 41, "AdjustmentLand", float),
    (12, 42, "AdjustmentImprove", float),
    (12, 43, "AdjustmentFarm", float),
    (12, 44, "ValueLandBreaker", float),
    (12, 45, "ValueImproveBreaker", float),
    (12, 46, "ValueNonHomeLandBreaker", float),
    (12, 47, "ValueNonHomeImprBreaker", float),
    (12, 48, "ValueAptLand", float),
    (12, 49, "ValueAptImpr", float),
    (12, 50, "ValueCareLandBreaker", float),
    (12, 51, "ValueCareImproveBreaker", float),
    (12, 52, "ValueFarmBreaker", float),
    (12, 53, "ValueMobileBreaker", float),
    (12, 54, "Land3Breaker", float),
    (12, 55, "Improve3Breaker", float),
    (12, 56, "ClassifiedLand", float),
    (12, 57, "DeededAcreage", float),
    (10, 58, "AppraisalDate", None),
    (2, 59, "ReasonCodeChange", str),
    (12, 60, "PriorValueLand", float),
    (12, 61, "PriorImprove", float),
    (5, 62, "AdjustmentFactor", float),
    (500, 63, "LegalDescription", str),
    (1, 64, "Anonymous", str),
    (12, 65, "CurrentValueLand", float),
    (12, 66, "CurrentValueImprove", float),
    (12, 67, "CurrentValueTotal", float),
]


def load_parcel_file():
    """Load parcel file

    Returns
    -------
    df : pd.DataFrame
        DataFrame containing data on parcels
    """
    # real_fname = f"RealParcel_{county}_18_2018P2019.txt"

    fname_stem = f"RealParcel_"
    ext = ".txt"

    dtypes = {x[2]: x[3] for x in PARCEL_FILE_COLS if x[3] is not None}
    date_cols = tuple(x[1] for x in PARCEL_FILE_COLS if x[3] is None)
    col_widths = list(x[0] for x in PARCEL_FILE_COLS)
    col_names = list(x[2] for x in PARCEL_FILE_COLS)

    df = pd.concat(
        [
            pd.read_fwf(
                DATA_DIR.joinpath(fname),
                widths=col_widths,
                names=col_names,
                skipfooter=1,
                dtypes=dtypes,
                # infer_date_cols=date_cols,
                skiprows=1,
            )
            for fname in DATA_DIR.glob(f"{fname_stem}*{ext}")
        ]
    )

    for col, fmt in PARCEL_DATE_COLS:
        df.loc[:, col] = pd.to_datetime(df.loc[:, col], format=fmt)
    return df


if __name__ == "__main__":

    df = load_parcel_file()

    print(" ")
