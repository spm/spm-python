from spm.__wrapper__ import Runtime


def fiff_make_dir_tree(*args, **kwargs):
  """   
    [tree, last] = fiff_make_dir_tree(fid,dir,start,indent)  
     
    Create the directory tree structure  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_make_dir_tree.m)
  """

  return Runtime.call("fiff_make_dir_tree", *args, **kwargs)
