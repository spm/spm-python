from spm.__wrapper__ import Runtime


def fiff_open(*args, **kwargs):
  """   
    [fid, tree, dir] = fiff_open(fname)  
     
    Open a fif file and provide the directory of tags  
     
    fid     the opened file id  
    tree    tag directory organized into a tree  
    dir     the sequential tag directory  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_open.m)
  """

  return Runtime.call("fiff_open", *args, **kwargs)
