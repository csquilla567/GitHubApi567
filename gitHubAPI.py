'''
Created on Feb 11, 2018

@author: Caroline Squillante

gitHubAPI.py program to pull repos and number of commits per repo for a user
'''
#edited for Project 1

import requests
import json

def get_username(userId):
    response = requests.get('https://api.github.com/users/' + userId + '/repos')
    if response.ok:
        return response
    else:
        return None

def get_repo_commits(userId, repoName):
    response = requests.get('https://api.github.com/repos/' + userId + '/' + repoName + '/commits')
    if response.ok:
        return response
    else:
        return None

def repoNames(userId):
    
    #r = requests.get('https://api.github.com/users/' + userId + '/repos')
    r = get_username(userId)
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
    #r = get_repo_commits(userId, repoName)
    commitData = json.loads(r.text)
    return len(commitData)


if __name__ == "__main__":
    user = input("Enter Github username: ")
    print("User: " + user)

    repos = repoNames(user)
    
    if len(repos) > 0:
        for r in repos:
            print("Repo: " + r + " Number of Commits: " + str(commitNum(user, r))) 
