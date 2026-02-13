import pandas as pd

def getMassTable(filename="masses.dat"):
    df = pd.read_csv(
        filename,
        comment="#",
        delim_whitespace=True,
        names=["isotope", "mass"]
    )
    return dict(zip(df["isotope"], df["mass"]))
