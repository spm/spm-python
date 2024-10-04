from spm.__wrap__ import _Runtime


def _bst_prctile(*args, **kwargs):
  """  BST_PRCTILE: Returns the percentile value in vector  
     
    USAGE: value = bst_prctile(vector, percentile)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/private/bst_prctile.m)
  """

  return _Runtime.call("bst_prctile", *args, **kwargs)
