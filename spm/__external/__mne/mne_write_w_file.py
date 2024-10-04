from spm.__wrap__ import _Runtime


def mne_write_w_file(*args, **kwargs):
  """  mne_write_w_file(filename, w)  
     
     writes a binary 'w' file  
     
     filename - name of file to write to  
     w        - a structure with the following fields:  
     
    vertices - vector of vertex indices (0-based)  
    data     - vector of data values  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_write_w_file.m)
  """

  return _Runtime.call("mne_write_w_file", *args, **kwargs)
