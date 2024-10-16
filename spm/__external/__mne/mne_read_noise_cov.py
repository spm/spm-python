from spm.__wrapper__ import Runtime


def mne_read_noise_cov(*args, **kwargs):
  """   
    [cov] = mne_read_noise_cov(fname)  
     
    Reads a noise-covariance matrix from a fiff file  
     
    fname      - The name of the file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_noise_cov.m)
  """

  return Runtime.call("mne_read_noise_cov", *args, **kwargs)
