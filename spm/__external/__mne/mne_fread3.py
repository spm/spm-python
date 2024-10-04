from spm.__wrap__ import _Runtime


def mne_fread3(*args, **kwargs):
  """   
    [retval] = mne_fread3(fid)  
    read a 3 byte integer out of a file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_fread3.m)
  """

  return _Runtime.call("mne_fread3", *args, **kwargs)
