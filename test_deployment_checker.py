import unittest
import subprocess
import sys
import os

class TestDeploymentChecker(unittest.TestCase):
    """Tests for the deployment checker script"""
    
    def test_checker_script_exists(self):
        """Test that the deployment checker Python script exists"""
        self.assertTrue(os.path.exists('check_deployment.py'))
    
    def test_checker_bash_script_exists(self):
        """Test that the deployment checker bash script exists"""
        self.assertTrue(os.path.exists('check_deployment.sh'))
    
    def test_checker_batch_script_exists(self):
        """Test that the deployment checker batch script exists"""
        self.assertTrue(os.path.exists('check_deployment.bat'))
    
    def test_checker_bash_script_executable(self):
        """Test that the bash script is executable"""
        if os.path.exists('check_deployment.sh'):
            self.assertTrue(os.access('check_deployment.sh', os.X_OK))
    
    def test_checker_imports(self):
        """Test that the checker script can be imported"""
        try:
            import check_deployment
            self.assertTrue(hasattr(check_deployment, 'check_git_status'))
            self.assertTrue(hasattr(check_deployment, 'check_dependencies'))
        except ImportError as e:
            self.fail(f"Could not import check_deployment: {e}")
    
    def test_git_status_function(self):
        """Test the git status checking function"""
        from check_deployment import check_git_status
        # This will return False due to uncommitted test file itself
        # but it should execute without errors
        result = check_git_status()
        self.assertIsInstance(result, bool)
    
    def test_force_flag_behavior(self):
        """Test that force flag is recognized"""
        # Just verify the script runs with --force flag without crashing
        result = subprocess.run(
            [sys.executable, 'check_deployment.py', '--force'],
            capture_output=True,
            text=True,
            timeout=10
        )
        # Script should run without error (even if it fails on dependencies)
        # The important thing is that --force is accepted as a valid argument
        self.assertIn('deployment check', result.stdout.lower())

if __name__ == '__main__':
    unittest.main()
