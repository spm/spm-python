from spm.__wrapper__ import Runtime


def readCTFMRI(*args, **kwargs):
  """   Version 1.2: 25 April 2007   Module readCPersist changed and removed from this listing.  
     Version 1.1: 19 April 2007   No changes since v1.0  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/ctf/readCTFMRI.m)
  """

  return Runtime.call("readCTFMRI", *args, **kwargs)
