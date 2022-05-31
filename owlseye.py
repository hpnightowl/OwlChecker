import argparse
import pandas as pd
# it is a version check why owlseye name? because it will look for the latest version of the program continuously 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a program to check the version of the program")
    parser.add_argument("-i", "--input", help="input file", required=True, nargs=2)
    args = parser.parse_args()
    data = pd.read_csv(args.input[0])
    check_pkg = args.input[1]
    print(check_pkg)
    repo_link = data['repo']
    repo_name = data['name']

print("Repo Link: " + repo_link)
print("Repo Name: " + repo_name)