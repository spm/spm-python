from spm.__wrap__ import _Runtime


def readCPersist(*args, **kwargs):
  """   Version 1.2   24 April 2007   Modified to close the CPersist file if a really huge  
     taglength is encountered.  Recently discovered .acq files with the string 'ssss' added  
     at the end of the file after the final 'EndofParameters' string.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/ctf/readCPersist.m)
  """

  return _Runtime.call("readCPersist", *args, **kwargs)
