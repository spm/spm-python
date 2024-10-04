from spm.__wrap__ import _Runtime


def writeMarkerFile(*args, **kwargs):
  """   Version 1.0   27 Oct. 2006  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/ctf/writeMarkerFile.m)
  """

  return _Runtime.call("writeMarkerFile", *args, **kwargs, nargout=0)
