### Referenced from [Toptal](https://www.toptal.com/python/an-introduction-to-mocking-in-python)

---
### Python file deletion to explain [unittest.mock](https://docs.python.org/3/library/unittest.mock-examples.html)

#### 3 types of unit test implementation in [test_delete_file.py](test_delete_file.py):

1. [FileDeleteTestCase](test_delete_file.py#L34)
   1. Advantages:
      - the [file_delete](file_deletion.py#L4) method is somewhat tested
     
   2. Drawbacks:
      - a temporary file is created and then deleted each time the test is run.
      -  no way of testing whether the [file_delete](file_deletion.py#L4) method properly passes the argument down to the os.remove() call 
 
2. [FileDeleteTestCaseWithMocking](test_delete_file.py#L60)
   1. Advantages:
      - the os.remove() call in the [file_delete](file_deletion.py#L4) method is tested with the right arguments
   
   2. Drawbacks:
        - it would be better mocking the os module itself rather than file_delete.os. For example, if the 'tempfile' module
          is to be mocked in a different module is another project, 'newProject.app.example_function', the mock will need to be applied to
          'newProject.app.tempfile', since each module has its own import.
          [file_delete](file_deletion.py#L4) method will have its own 'os' module at runtime.
          It's safer to mock an item where it is implemented, not where it came from

3. [FileDeleteTestCaseWithMockingOS](test_delete_file.py#L92)
   - The main advantage is that we can check and validate that the internal functionality of [file_delete](file_deletion.py#L4) method is called without any side effects


---