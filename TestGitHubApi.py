'''
Created on Feb 12, 2018

@author: Caroline Squillante
'''
import unittest
from gitHubAPI import repoNames, commitNum

class TestGithub(unittest.TestCase):
    
    def testRepo1(self):
        allRepos = repoNames('csquillz')
        self.assertGreaterEqual(len(allRepos), 1)
        self.assertIn('SSW',allRepos)

    def testRepo2(self):
        allRepos = repoNames('csquilla567')
        self.assertGreaterEqual(len(allRepos), 2)
        self.assertIn('Triangle567',allRepos)
        self.assertIn('GitHubApi567',allRepos)
    
    def testRepo3(self):
        allRepos = repoNames('karuaan')
        self.assertGreaterEqual(len(allRepos), 7)
        self.assertIn('ssw555CKMM2018Spring',allRepos)
        self.assertIn('CS-546-Web-Programming',allRepos)
        self.assertIn('karuaan.github.io',allRepos)
        self.assertIn('Android-Projects',allRepos)
        self.assertIn('Systems-Programming-',allRepos)
        self.assertIn('MusicMeld',allRepos)
        self.assertIn('Ratemycourse.com',allRepos)
            
    def testNumCommits1(self):
        self.assertGreaterEqual(commitNum('csquillz','SSW'),30)
        
    def testNumCommits2(self):
        self.assertGreaterEqual(commitNum('csquilla567','Triangle567'),4)
        
    def testNumCommits3(self):
        self.assertGreaterEqual(commitNum('karuaan','ssw555CKMM2018Spring'),23)
        self.assertGreaterEqual(commitNum('karuaan','CS-546-Web-Programming'),1)
        self.assertGreaterEqual(commitNum('karuaan','karuaan.github.io'),2)
        self.assertGreaterEqual(commitNum('karuaan','Android-Projects'),2)
        self.assertGreaterEqual(commitNum('karuaan','Systems-Programming-'),18)
        self.assertGreaterEqual(commitNum('karuaan','MusicMeld'),6)
        self.assertGreaterEqual(commitNum('karuaan','Ratemycourse.com'),6)
        
    def testInvalidInfo(self):
        allRepos = repoNames('csquillz9304')
        self.assertEqual(len(allRepos), 0)
        
        
        
