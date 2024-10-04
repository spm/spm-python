from spm.__wrap__ import _Runtime


def spm_data_hdr_read(*args, **kwargs):
  """  Get data information from file  
    FORMAT V = spm_data_hdr_read(P)  
    P        - a char or cell array of filenames  
     
    V        - a structure array containing data information  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_data_hdr_read.m)
  """

  return _Runtime.call("spm_data_hdr_read", *args, **kwargs)
