from spm.__wrap__ import _Runtime


def fiff_rename_list(*args, **kwargs):
  """fiff_rename_list is a function.  
      lst = fiff_rename_list(lst, ch_rename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_rename_list.m)
  """

  return _Runtime.call("fiff_rename_list", *args, **kwargs)
