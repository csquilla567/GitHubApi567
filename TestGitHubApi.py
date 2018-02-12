'''
Created on Feb 12, 2018

@author: Caroline Squillante
'''
import unittest
from gitHubAPI import repoNames, commitNum

class TestGithub(unittest.TestCase):
    
    def testRepo1(self):
        repos = repoNames('csquillz')
        self.assertIn('SSW',repos)

    def testRepo2(self):
        repos = repoNames('csquilla567')
        self.assertIn('Triangle567',repos)
        self.assertIn('GitHubApi567',repos)
        
        
    def testNumCommits(self):
        self.assertGreaterEqual(commitNum('csquillz','SSW'),30)
        self.assertGreaterEqual(commitNum('csquilla567','Triangle567'),4)
        
        