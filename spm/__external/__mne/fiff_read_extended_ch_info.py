from spm.__wrap__ import _Runtime


def fiff_read_extended_ch_info(*args, **kwargs):
  """fiff_read_extended_ch_info is a function.  
      [chs, ch_rename] = fiff_read_extended_ch_info(chs, meas_info, fid)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_extended_ch_info.m)
  """

  return _Runtime.call("fiff_read_extended_ch_info", *args, **kwargs)
