from spm.__wrap__ import _Runtime


def fiff_write_ch_infos(*args, **kwargs):
  """fiff_write_ch_infos is a function.  
      cals = fiff_write_ch_infos(fid, chs, reset_range, ch_rename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_ch_infos.m)
  """

  return _Runtime.call("fiff_write_ch_infos", *args, **kwargs)
