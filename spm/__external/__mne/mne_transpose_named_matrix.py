from spm.__wrapper__ import Runtime


def mne_transpose_named_matrix(*args, **kwargs):
  """   
    [res] = mne_transpose_named_matrix(mat)  
     
    Transpose a named matrix  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_transpose_named_matrix.m)
  """

  return Runtime.call("mne_transpose_named_matrix", *args, **kwargs)
