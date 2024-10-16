from spm.__wrapper__ import Runtime


def mne_fwrite3(*args, **kwargs):
  """   
    mne_fwrite(fid, val)  
    write a 3 byte integer to a file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_fwrite3.m)
  """

  return Runtime.call("mne_fwrite3", *args, **kwargs, nargout=0)
