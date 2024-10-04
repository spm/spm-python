from spm.__wrap__ import _Runtime


def mne_write_cov(*args, **kwargs):
  """   
     
      mne_write_cov(fid,cov)  
     
      Write a covariance matrix to an open file  
     
      fid     - an open file id  
      cov     - the covariance matrix to write  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_write_cov.m)
  """

  return _Runtime.call("mne_write_cov", *args, **kwargs, nargout=0)
