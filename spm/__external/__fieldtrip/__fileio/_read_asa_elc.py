from spm.__wrapper__ import Runtime


def _read_asa_elc(*args, **kwargs):
  """  READ_ASA_ELC reads electrodes from an ASA electrode file  
    converting the units to mm  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_asa_elc.m)
  """

  return Runtime.call("read_asa_elc", *args, **kwargs)
