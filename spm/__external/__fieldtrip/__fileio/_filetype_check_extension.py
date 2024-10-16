from spm.__wrapper__ import Runtime


def _filetype_check_extension(*args, **kwargs):
  """  FILETYPE_CHECK_EXTENSION helper function to determine the file type  
    by performing a case insensitive string comparison of the extension.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/filetype_check_extension.m)
  """

  return Runtime.call("filetype_check_extension", *args, **kwargs)
