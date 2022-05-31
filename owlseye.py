import argparse
import pandas as pd
# it is a version check why owlseye name? because it will look for the latest version of the program continuously 

# fetches json data
def fetch_pkg():
    pass

# gets the csv data
def get_data(args):
    data = pd.read_csv(args.input[0])
    return data

# converts the data from input file
def data_prep(data):
    repo_name = data['name']
    repo_url = data['repo']
    repo_name.to_numpy()
    repo_url.to_numpy()
    return repo_name, repo_url

# Where cooking begins
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a program to check the version of the program")
    parser.add_argument("-i", "--input", help="input file", required=True, nargs=2)
    args = parser.parse_args()
    data = get_data(args)
    name, url = data_prep(data)
    