from spm.__wrap__ import _Runtime


def readCTFds(*args, **kwargs):
  """  ************************************************************************  
     
      This program is provided to users of CTF MEG systems as a courtesy only.  
      It's operation has not been verified for clinical use.  
      Please do not redistribute it without permission from CTF Systems Inc.  
     
    ************************************************************************  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/ctf/readCTFds.m)
  """

  return _Runtime.call("readCTFds", *args, **kwargs)
