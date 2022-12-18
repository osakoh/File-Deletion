"""
unittest supports some object-oriented concepts:
i) test fixture: represents the preparation needed to perform one or more tests, and any associated cleanup actions.
This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

ii) test case: represents the individual unit of testing. It checks for a specific response to a particular
set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

iii) test suite: is a collection of test cases, test suites, or both.
It is used to aggregate tests that should be executed together.

iv) test runner
A test runner is a component which orchestrates the execution of tests and provides the outcome to the user.
The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.
"""
# Unlike a Unix shell, Python does not do any automatic path expansions
# path parameters are either strings or bytes
import os
# creates temporary files and directories consisting of,
# TemporaryFile, NamedTemporaryFile, TemporaryDirectory, and SpooledTemporaryFile
import tempfile
import unittest

from file_deletion import file_delete


class FileDeleteTestCase(unittest.TestCase):
    # original(not escaped): C:\TEMP, C:\TMP, \TEMP, & \TMP
    # escaped backslash(\):  C:\\TEMP, C:\\TMP, \\TEMP, & \\TMP
    """
    tempfile.gettempdir(): returns the name of the directory used for temporary files
    On Windows: directories, C:\\TEMP, C:\\TMP, \\TEMP, and \\TMP, in that order.
    Other platforms, the directories /tmp, /var/tmp, and /usr/tmp, in that order
    """
    tmpFilePath = os.path.join(tempfile.gettempdir(), "tmp-testfile.txt")
    print(f"\n*********************************************************")
    # tmpFilePath: C|D:\Users\<username>\AppData\Local\Temp\tmp-testfile.txt
    print(f"tmpFilePath: {tmpFilePath}")
    print(f"*********************************************************\n")

    # instructions to be executed before each test
    def setUp(self) -> None:
        with open(self.tmpFilePath, "w") as f:
            f.write("Content of file")

    def test_file_delete(self):
        """ tests file deletion method """
        file_delete(self.tmpFilePath)
        actual = os.path.isfile(self.tmpFilePath)
        expected = "Failed to remove the file."
        # Check that the expression is false
        self.assertFalse(actual, expected)
