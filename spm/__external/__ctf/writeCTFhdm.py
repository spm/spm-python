from spm.__wrap__ import _Runtime


def writeCTFhdm(*args, **kwargs):
  """   Version 1.1   20 April 2007   Modified to make sure that clinical-0ise message and   
                                   creator software are not repeated.  
                                   Test date.  
                   22 March 2007.  Modified to write v6.0 .hdm files which have additional  
                                   fields in MultiSphere_Data.  Check that the .hdm version  
                                   number is compatible with the fields included in  
                                   MultiSphere_Data.  
     Creates a CTF-compatible head model file from structure hdm  
     Structure hdm is in the format produced by readCTFhdm.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/ctf/writeCTFhdm.m)
  """

  return _Runtime.call("writeCTFhdm", *args, **kwargs, nargout=0)
