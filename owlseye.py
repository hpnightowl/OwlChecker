import argparse
import pandas as pd
# it is a version check why owlseye name? because it will look for the latest version of the program continuously 

def compare_version(version,args):
    satisfied = []
    for i in range(len(version)):
        if version[i] >= args.input[1].split('@')[1]:
            satisfied.append(True)
        else:
            satisfied.append(False)
    return satisfied

# fetches json data
def fetch_pkg(n,data,args):
    version = []
    for link in range(n):
        s = data[link].replace("github.com", "raw.githubusercontent.com")
        s+= "/master/package.json"
        dependen_s = pd.read_json(s)
        current_version = dependen_s['dependencies'][args.input[1].split('@')[0]][1:]
        version.append(current_version)
    return version

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
    version = fetch_pkg(len(data),url,args)
    print(version)
    version_satisfied = compare_version(version,args)
    print(version_satisfied)