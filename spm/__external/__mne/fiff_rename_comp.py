from spm.__wrapper__ import Runtime


def fiff_rename_comp(*args, **kwargs):
  """fiff_rename_comp is a function.  
      comp = fiff_rename_comp(comp, ch_rename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_rename_comp.m)
  """

  return Runtime.call("fiff_rename_comp", *args, **kwargs)
