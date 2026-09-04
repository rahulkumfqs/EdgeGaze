# test_edgegaze.py
"""
Tests for EdgeGaze module.
"""

import unittest
from edgegaze import EdgeGaze

class TestEdgeGaze(unittest.TestCase):
    """Test cases for EdgeGaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EdgeGaze()
        self.assertIsInstance(instance, EdgeGaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EdgeGaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
