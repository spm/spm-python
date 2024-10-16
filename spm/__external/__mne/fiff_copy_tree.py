from spm.__wrapper__ import Runtime


def fiff_copy_tree(*args, **kwargs):
  """   
       fiff_copy_tree(fidin, in_id, nodes, fidout)  
     
       Copies directory subtrees from fidin to fidout  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_copy_tree.m)
  """

  return Runtime.call("fiff_copy_tree", *args, **kwargs, nargout=0)
