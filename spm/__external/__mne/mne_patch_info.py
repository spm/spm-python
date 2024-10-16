from spm.__wrapper__ import Runtime


def mne_patch_info(*args, **kwargs):
  """   
    [pinfo] = mne_patch_info(nearest)  
     
    Generate the patch information from the 'nearest' vector in a source space  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_patch_info.m)
  """

  return Runtime.call("mne_patch_info", *args, **kwargs)
