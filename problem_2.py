import os

def fine_files_util(suffix, path, file_found_paths):
    if os.path.isfile(path) and path.endswith(suffix):
        return file_found_paths + [path]

    if os.path.isdir(path):
        for directory in os.listdir(path):
            file_found_paths = fine_files_util(suffix, os.path.join(path, directory), file_found_paths)
    
    return file_found_paths


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
      
    Returns:
       a list of paths
    """
    if suffix is None or path is None:
        result = []
    else:
        result = fine_files_util(suffix, path, [])
    return result if len(result) > 0 else 'Directory path/Suffix not found'

# Test case 1
# Expected: ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
print(find_files('.c', './testdir'))

# Test case 2
# Expected: Directory path/Suffix not found for the rest because the file didn't exist in the first place
print(find_files('.csv', './testdir'))
print(find_files('invalid', './testdir'))  
print(find_files('.c', 'invalid')) 

# Test case 3
# Expected: Directory path/Suffix not found for both because there's no such path exist or directory exist
print(find_files(None, './testdir')) 
print(find_files(None, None)) 
