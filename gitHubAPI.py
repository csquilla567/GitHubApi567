'''
Created on Feb 11, 2018

@author: Caroline Squillante
'''

import requests
import json

def repoNames(userId):
    
    r = requests.get("https://api.github.com/users/" + userId + "/repos")
    repos = []
    repoData = json.loads(r.text)
    
    for info in repoData:
        repos += [info.get('name')]
    return repos
    
def commitNum(userId, repoName):
    
    r = requests.get('https://api.github.com/repos/' + userId + '/' + repoName + '/commits')
    commitData = json.loads(r.text)
    return len(commitData)

if __name__ == "__main__":
    user = input("Enter a Github username to view their repositories ")
    print("User: " + user)

    repos = repoNames(user)

    for r in repos:
        print("Repo: " + r + " Number of Commits: " + str(commitNum(user,r)))
        
        
        
        
