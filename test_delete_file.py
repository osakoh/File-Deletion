"""
unittest supports some object-oriented concepts:
i) test fixture: represents the preparation needed to perform one or more tests, and any associated cleanup actions.
This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

ii) test case: represents the individual unit of testing. It checks for a specific response to a particular
set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

iii) test suite: is a collection of test cases, test suites, or both.
Used to aggregate tests that should be executed together.

iv) test runner: a component which orchestrates the execution of tests and provides the outcome to the user.
The runner may use a graphical interface, a textual interface, or return a
special value to indicate the results of executing the tests.
"""
# print(f"\n*********************************************************")
# tmpFilePath: C:\Users\<username>\AppData\Local\Temp\tmp-testfile.txt
# print(f"tmpFilePath: {tmpFilePath}")
# print(f"*********************************************************\n")

# Unlike a Unix shell, Python does not do any automatic path expansions
# path parameters are either strings or bytes
# creates temporary files and directories consisting of,
# TemporaryFile, NamedTemporaryFile, TemporaryDirectory, and SpooledTemporaryFile
import unittest
from unittest import mock

from file_deletion import file_delete


# class FileDeleteTestCase(unittest.TestCase):
#     """
#     tempfile.gettempdir(): returns the name of the directory used for temporary files
#     On Windows: directories, C:\\TEMP, C:\\TMP, \\TEMP, and \\TMP, in that order.
#     Other platforms, the directories /tmp, /var/tmp, and /usr/tmp, in that order
#
#     Problems with this implementation style:
#     i) a temporary file is created and then deleted each time the test is run.
#     ii) no way of testing whether the file_delete method properly passes the argument down to the os.remove() call
#     """
#     tmpFilePath = os.path.join(tempfile.gettempdir(), "tmp-testfile.txt")
#
#     # instructions to be executed before each test
#     def setUp(self) -> None:
#         with open(self.tmpFilePath, "w") as f:
#             f.write("Content of file")
#
#     def test_file_delete(self):
#         """ tests file deletion method """
#         file_delete(self.tmpFilePath)
#         actual = os.path.isfile(self.tmpFilePath)
#         expected = "Failed to remove the file."
#         # Check that the expression is false
#         self.assertFalse(actual, expected)


# class FileDeleteTestCaseWithMocking(unittest.TestCase):
#     """
#     tempfile.gettempdir(): returns the name of the directory used for temporary files
#     On Windows: directories, C:\\TEMP, C:\\TMP, \\TEMP, and \\TMP, in that order.
#     Other platforms, the directories /tmp, /var/tmp, and /usr/tmp, in that order
#
#     Adv:
#     i) the os.remove() call in the file_delete method is tested with the right arguments
#
#     Problems:
#     i) it's better to mock the os module itself rather than file_delete.os. For example, if the 'tempfile' module
#     is to be mocked in this project, 'newProject.app.example_function', the mock will need to be applied to
#     'newProject.app.tempfile', since each module has its own import.
#     'file_delete' will have its own 'os' module at runtime.
#     It's safer to mock an item where it is implemented, not where it came from
#     """
#     tmpFilePath = os.path.join(tempfile.gettempdir(), "tmp-testfile.txt")
#
#     # instructions to be executed before each test
#     def setUp(self) -> None:
#         with open(self.tmpFilePath, "w") as f:
#             f.write("Content of file")
#
#     @mock.patch("file_deletion.os")
#     def test_file_delete(self, mock_os_call):
#         """ tests file deletion method """
#         file_delete(self.tmpFilePath)
#
#         # check that the file_delete method called os.remove() with the correct arguments
#         mock_os_call.remove.assert_called_with(self.tmpFilePath)


class FileDeleteTestCaseWithMockingOS(unittest.TestCase):
    """
    tempfile.gettempdir(): returns the name of the directory used for temporary files
    On Windows: directories, C:\\TEMP, C:\\TMP, \\TEMP, and \\TMP, in that order.
    Other platforms, the directories /tmp, /var/tmp, and /usr/tmp, in that order

    Adv:
    i) the os.remove() call in the file_delete method is tested with the right arguments

    Problems:
    i) it's better to mock the os module itself rather than file_delete.os. For example, if the 'tempfile' module
    is to be mocked in this project, 'newProject.app.example_function', the mock will need to be applied to
    'newProject.app.tempfile', since each module has its own import.
    'file_delete' will have its own 'os' module at runtime.
    It's safer to mock an item where it is implemented, not where it came from
    """

    @mock.patch("file_deletion.os.path")
    @mock.patch("file_deletion.os")
    def test_file_delete(self, mock_os, mock_os_path):
        """ tests file deletion method """
        # set up the mock for 'os.path.isfile(filename) => returns True or False'
        # file doesn't exist by returning False
        mock_os_path.isfile.return_value = False
        # perform delete; call file_delete method
        file_delete("ex/path")
        # check that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, msg="File not present")
        # make file exist by returning True
        mock_os_path.isfile.return_value = True
        # perform delete; call file_delete method
        file_delete("ex/path")
        # check that the file_delete method called os.remove() with the correct arguments
        mock_os.remove.assert_called_with("ex/path")
