from spm.__wrapper__ import Runtime


def _read_asa_msr(*args, **kwargs):
  """  READ_ASA_MSR reads EEG or MEG data from an ASA data file  
    converting the units to uV or fT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_asa_msr.m)
  """

  return Runtime.call("read_asa_msr", *args, **kwargs)
