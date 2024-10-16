from spm.__wrapper__ import Runtime


def _isricohmegfile(*args, **kwargs):
  """  The extentions, .con, .ave, and .mrk are common between Ricoh and Yokogawa systems.  
    isricohmegfile idetifies whether the file is generated from Ricoh system or not.  
    This function uses a function in YOKOGAWA_MEG_READER toolbox, getYkgwHdrSystem.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/isricohmegfile.m)
  """

  return Runtime.call("isricohmegfile", *args, **kwargs)
