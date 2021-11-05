import csv


def get_auth_endpoints():
    with open("test_data/auth_endpoints.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for el in reader:
            yield el


auth_endpoints = get_auth_endpoints()
