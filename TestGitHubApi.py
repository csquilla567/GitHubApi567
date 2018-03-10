'''
Created on Feb 12, 2018

@author: Caroline Squillante
'''
import unittest
from gitHubAPI import repoNames, commitNum
from unittest.mock import Mock, patch

class TestGithub(unittest.TestCase):
    @patch('TestGitHubApi.repoNames')
    def testRepo1(mock_repo_names, self):
        fake_json = {'name': 'SSW'}
        mock_repo_names.return_value = Mock()
        mock_repo_names.return_value.json.return_value = [fake_json]
        
        allRepos = repoNames('csquillz')
        #self.assertTrue(mock_repo_names.called)
        self.assertGreaterEqual(len(allRepos), 1)
        self.assertIn('SSW',allRepos)

    @patch('TestGitHubApi.repoNames')
    def testRepo2(mock_repo_names, self):
        fake_json = [{'name': 'Triangle567'},
                     {'name': 'GitHubApi567'},
                     {'name': 'example-python'},
                     {'name': 'sq-com_example_standard-sqscanner-travis'}]
        mock_repo_names.return_value = Mock()
        mock_repo_names.return_value.json.return_value = fake_json
        
        allRepos = repoNames('csquilla567')
        #self.assertTrue(mock_repo_names.called)
        self.assertGreaterEqual(len(allRepos), 2)
        self.assertIn('Triangle567',allRepos)
        self.assertIn('GitHubApi567',allRepos)

    @patch('TestGitHubApi.repoNames')
    def testRepo3(mock_repo_names, self):
        fake_json = [{'name': 'ssw555CKMM2018Spring'},
                     {'name': 'CS-546-Web-Programming'},
                     {'name': 'karuaan.github.io'},
                     {'name': 'Android-Projects'},
                     {'name': 'Systems-Programming-'},
                     {'name': 'MusicMeld'},
                     {'name': 'Ratemycourse.com'}]
        mock_repo_names.return_value = Mock()
        mock_repo_names.return_value.json.return_value = fake_json
        
        allRepos = repoNames('karuaan')

        #self.assertTrue(mock_repo_names.called)
        self.assertGreaterEqual(len(allRepos), 7)
        self.assertIn('ssw555CKMM2018Spring',allRepos)
        self.assertIn('CS-546-Web-Programming',allRepos)
        self.assertIn('karuaan.github.io',allRepos)
        self.assertIn('Android-Projects',allRepos)
        self.assertIn('Systems-Programming-',allRepos)
        self.assertIn('MusicMeld',allRepos)
        self.assertIn('Ratemycourse.com',allRepos)

    @patch('TestGitHubApi.commitNum')
    def testNumCommits1(mock_commit_num, self):
        mock_commit_num.return_value = Mock(30)
        self.assertGreaterEqual(commitNum('csquillz','SSW'),30)
        #self.assertTrue(mock_commit_num.called)

    @patch('TestGitHubApi.repoNames')
    def testNumCommits2(mock_commit_num, self):
        mock_commit_num.return_value = Mock(50)
        self.assertGreaterEqual(commitNum('csquilla567','Triangle567'),4)
        #self.assertTrue(mock_commit_num.called)

    @patch('TestGitHubApi.commitNum')
    def testNumCommits3(mock_commit_num, self):
        mock_commit_num.return_value = Mock(30)
        self.assertGreaterEqual(commitNum('karuaan','ssw555CKMM2018Spring'),23)
        self.assertGreaterEqual(commitNum('karuaan','CS-546-Web-Programming'),1)
        self.assertGreaterEqual(commitNum('karuaan','karuaan.github.io'),2)
        self.assertGreaterEqual(commitNum('karuaan','Android-Projects'),2)
        self.assertGreaterEqual(commitNum('karuaan','Systems-Programming-'),18)
        self.assertGreaterEqual(commitNum('karuaan','MusicMeld'),6)
        self.assertGreaterEqual(commitNum('karuaan','Ratemycourse.com'),6)
        #self.assertTrue(mock_commit_num.called)

    @patch('TestGitHubApi.repoNames')
    def testInvalidInfo(mock_repo_name, self):
        mock_repo_name.return_value = Mock(0)
        allRepos = repoNames('csquillz9304')
        self.assertEqual(len(allRepos), 0)
        #self.assertTrue(mock_repo_name.called)

if __name__ == '__main__':
    print("Running unit test")
    unittest.main()        
        
