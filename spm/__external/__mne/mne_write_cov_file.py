from spm.__wrap__ import _Runtime


def mne_write_cov_file(*args, **kwargs):
  """   
      function mne_write_cov_file(name,cov)  
     
      Write a complete fif file containing a covariance matrix  
     
      fname    filename  
      cov      the covariance matrix to write  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_write_cov_file.m)
  """

  return _Runtime.call("mne_write_cov_file", *args, **kwargs, nargout=0)
