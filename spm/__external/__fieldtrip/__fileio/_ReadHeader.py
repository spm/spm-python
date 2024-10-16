from spm.__wrapper__ import Runtime


def _ReadHeader(*args, **kwargs):
  """  H = ReadHeader(fp)  
     
     Reads NSMA header, leaves file-read-location at end of header  
     
     INPUT:  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/ReadHeader.m)
  """

  return Runtime.call("ReadHeader", *args, **kwargs)
