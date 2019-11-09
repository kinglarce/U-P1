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
    return fine_files_util(suffix, path, [])    

print(find_files('.c', './testdir'))