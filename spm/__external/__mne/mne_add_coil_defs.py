from spm.__wrap__ import _Runtime


def mne_add_coil_defs(*args, **kwargs):
  """   
    [res] = mne_add_coil_defs(chs,accuracy,coil_def_templates)  
     
    Add transformed coil definitions to the channel info  
     
    chs        - original channel definitions  
    accuracy   - desired accuracy (0, 1, or 2, defaults to 1)  
    templates  - coil definition templates  
                 (defaults to $MNE_ROOT/setup/mne/coil_def.dat or $MNE_ROOT/share/mne/coil_def.dat)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_add_coil_defs.m)
  """

  return _Runtime.call("mne_add_coil_defs", *args, **kwargs)
