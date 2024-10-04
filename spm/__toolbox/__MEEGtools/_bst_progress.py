from spm.__wrap__ import _Runtime


def _bst_progress(*args, **kwargs):
  """  Dummy function to be able to use BST code unmodified  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/private/bst_progress.m)
  """

  return _Runtime.call("bst_progress", *args, **kwargs)
