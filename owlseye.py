import sys
import pandas as pd
# it is a version check why owlseye name? because it will look for the latest version of the program continuously 

input_file = sys.argv[1]

data = pd.read_csv(input_file)

repo_link = data['repo']
repo_name = data['name']

print("Repo Link: " + repo_link)
print("Repo Name: " + repo_name)