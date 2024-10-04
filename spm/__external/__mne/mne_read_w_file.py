from spm.__wrap__ import _Runtime


def mne_read_w_file(*args, **kwargs):
  """   
    [w] = mne_read_w_file(filename)  
     
    Reads a binary w file into the structure w with the following fields  
     
    vertices - vector of vertex indices (0-based)  
    data     - vector of data values  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_w_file.m)
  """

  return _Runtime.call("mne_read_w_file", *args, **kwargs)
