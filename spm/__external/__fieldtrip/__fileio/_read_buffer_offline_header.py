from spm.__wrap__ import _Runtime


def _read_buffer_offline_header(*args, **kwargs):
  """  function [hdr, nameFlag] = read_buffer_offline_header(headerfile)  
     
    This function reads a FCDC buffer header from a binary file or text file  
     
    On return, nameFlag has one of the following values:  
      0 = No labels were generated (fMRI etc.)  
      1 = Fake labels were generated  
      2 = Got channel labels from chunk information  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_buffer_offline_header.m)
  """

  return _Runtime.call("read_buffer_offline_header", *args, **kwargs)
