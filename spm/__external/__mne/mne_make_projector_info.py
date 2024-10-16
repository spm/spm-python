from spm.__wrapper__ import Runtime


def mne_make_projector_info(*args, **kwargs):
  """   
    [proj,nproj] = mne_make_projector_info(info)  
     
    Make an SSP operator using the meas info  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_make_projector_info.m)
  """

  return Runtime.call("mne_make_projector_info", *args, **kwargs)
