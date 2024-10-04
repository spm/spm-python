from spm.__wrap__ import _Runtime


def mne_make_projector(*args, **kwargs):
  """   
    [proj,nproj,U] = mne_make_projector(projs,ch_names,bads)  
     
    proj     - The projection operator to apply to the data  
    nproj    - How many items in the projector  
    U        - The orthogonal basis of the projection vectors (optional)  
     
    Make an SSP operator  
     
    projs    - A set of projection vectors  
    ch_names - A cell array of channel names  
    bads     - Bad channels to exclude  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_make_projector.m)
  """

  return _Runtime.call("mne_make_projector", *args, **kwargs)
