from spm.__wrapper__ import Runtime


def mne_pick_channels_cov(*args, **kwargs):
  """   
    [cov] = mne_pick_channels_cov(orig,include,exclude)  
     
    Pick desired channels from a covariance matrix  
     
    orig      - The original covariance matrix  
    include   - Channels to include (if empty, include all available)  
    exclude   - Channels to exclude (if empty, do not exclude any)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_pick_channels_cov.m)
  """

  return Runtime.call("mne_pick_channels_cov", *args, **kwargs)
