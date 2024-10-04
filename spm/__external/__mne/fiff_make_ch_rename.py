from spm.__wrap__ import _Runtime


def fiff_make_ch_rename(*args, **kwargs):
  """fiff_make_ch_rename is a function.  
      ch_rename = fiff_make_ch_rename(chs)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_make_ch_rename.m)
  """

  return _Runtime.call("fiff_make_ch_rename", *args, **kwargs)
