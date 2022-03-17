import pandas as pd


def filter_contacts(filename: str) -> dict:
    all_contacts = pd.read_csv(filename)
    all_contacts = all_contacts[["Name", "Given Name"]]
    wishing_contacts = {}
    for row in all_contacts.iterrows():
        print(str(row["Name"]) + "  -  " + str(row["Given Name"]))
        wishing_contacts[str(row["Name"])] = str(row["Given Name"])
    return wishing_contacts
