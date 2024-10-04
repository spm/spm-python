from spm.__wrap__ import _Runtime


def _read_asa_msr(*args, **kwargs):
  """  READ_ASA_MSR reads EEG or MEG data from an ASA data file  
    converting the units to uV or fT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_asa_msr.m)
  """

  return _Runtime.call("read_asa_msr", *args, **kwargs)
