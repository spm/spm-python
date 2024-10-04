from spm.__wrap__ import _Runtime


def fiff_list_dir_tree(*args, **kwargs):
  """   
    fiff_list_dir_tree(fid, tree)  
     
    List the fiff directory tree structure  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_list_dir_tree.m)
  """

  return _Runtime.call("fiff_list_dir_tree", *args, **kwargs, nargout=0)
