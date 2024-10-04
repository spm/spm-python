from spm.__wrap__ import _Runtime


def mne_read_cov(*args, **kwargs):
  """   
    [cov] = mne_read_cov(fid,node,kind)  
     
    Reads a covariance matrix from a fiff file  
     
    fid       - an open file descriptor  
    node      - look for the matrix in here  
    cov_kind  - what kind of a covariance matrix do we want?  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_cov.m)
  """

  return _Runtime.call("mne_read_cov", *args, **kwargs)
