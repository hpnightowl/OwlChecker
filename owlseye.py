import argparse
import pandas as pd
import git
from github import Github
import requests
import json
# it is a version check why owlseye name? because it will look for the latest version of the program continuously 

# save only the false results location and make changes in that
save_false_i = []

# github api
def github(args):
    data = get_data(args)
    for i in save_false_i:
        s = data['repo'][i]
        s = s.replace("github.com", "raw.githubusercontent.com")
        s+= "/master/package.json"
        read_json = pd.read_json(s)
        
        # new_repo = git.Repo.init(data["name"][i])
        # my_repo = git.Repo(data["name"][i])
        # file_name = wget.download(s, data["name"][i])
        # g = Github("token")
        # user = g.get_user()
        # #repo = user.create_repo(data["name"][i])
        # git.Repo.clone_from(data['repo'][i], data['name'][i])
        # repo = git.Repo(data['name'][i])
        # with git.Repo.init(data["name"][i]).config_writer() as git_config:
        #     git_config.set_value('user', 'email', 'proaf@gmail.com')
        #     git_config.set_value('user', 'name', 'proaf')
        # git.Repo(data['name'][i])
        # read_json = pd.read_json(data["name"][i]+"/package.json")
        # read_json['dependencies'][args.input[1].split('@')[0]] = args.input[1].split('@')[1]
        # result = read_json.to_json(data['name'][i]+"/package.json")
        # repo.git.branch('update')
        # repo.git.checkout('update')
        # repo.index.add("package.json")
        # repo.index.commit("update version")
        # # # Create a new remote
        # remote = repo.create_remote('update', url='https://github.com/proaf/'+data["name"][i])
        # repo.remotes.update.push()

        headers={
            "Authorization": "token token_id",
            "Accept": "application/vnd.github.v3+json"
        }
        gitdata={
            "title": "update version",
            "body": "update version",
            "head": "update",
            "base": "master"
        }
        username = "proaf"
        repo_name = data["name"][i]
        #print(data['name'][i])
        repo_url = "https://api.github.com/repos/"+username+"/"+repo_name+"/pulls"
        response = requests.post(repo_url, data=json.dumps(gitdata), headers=headers)
        print(response.json())

def compare_version(version,args):
    satisfied = []
    for i in range(len(version)):
        if version[i] >= args.input[1].split('@')[1]:
            satisfied.append(True)
        else:
            satisfied.append(False)
            save_false_i.append(i)
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

def save_results(version, version_satisfied, args):
    data = get_data(args)
    data['version'] = version
    data['version_satisfied'] = version_satisfied
    data.to_csv('results.csv')

# Where cooking begins
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input file", required=True, nargs=2)
    args = parser.parse_args()
    data = get_data(args)
    name, url = data_prep(data)
    version = fetch_pkg(len(data),url,args)
    version_satisfied = compare_version(version,args)
    save_results(version, version_satisfied,args)
    github(args)