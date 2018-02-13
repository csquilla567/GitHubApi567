'''
Created on Feb 11, 2018

@author: Caroline Squillante

gitHubAPI.py program to pull repos and number of commits per repo for a user
'''

import requests
import json

def repoNames(userId):
    
    r = requests.get('https://api.github.com/users/' + userId + '/repos')
    repos = []
    repoData = json.loads(r.text)
    
    for info in repoData:
        try:
            repos += [info.get('name')]
        except (AttributeError):
            print('Error: unable to find repos for this user')
            return []
    return repos

    
def commitNum(userId, repoName):
    
    r = requests.get('https://api.github.com/repos/' + userId + '/' + repoName + '/commits')
    commitData = json.loads(r.text)
    return len(commitData)


if __name__ == "__main__":
    user = input("Enter Github username: ")
    print("User: " + user)

    repos = repoNames(user)
    
    if len(repos) > 0:
        for r in repos:
            print("Repo: " + r + " Number of Commits: " + str(commitNum(user, r))) 
