from spm.__wrapper__ import Runtime


def fiff_dir_tree_find(*args, **kwargs):
  """   
    [nodes] = fiff_dir_tree_find(tree,kind)  
     
    Find nodes of the given kind from a directory tree structure  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_dir_tree_find.m)
  """

  return Runtime.call("fiff_dir_tree_find", *args, **kwargs)
