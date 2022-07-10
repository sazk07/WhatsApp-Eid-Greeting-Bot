import pandas


def filter_contacts(filename) -> dict:
    all_contacts = pandas.read_csv(filename)
    all_contacts = all_contacts[["Name", "Given Name"]]
    wishing_contacts = dict()
    for _, row in all_contacts.iterrows():
        print(f"{str(row['Name'])} - {str(row['Given Name'])}")
        name_val = str(row["Name"])
        given_name_val = str(row["Given Name"])
        wishing_contacts[name_val] = given_name_val
    return wishing_contacts
