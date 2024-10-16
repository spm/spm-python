from spm.__wrapper__ import Runtime


def spm_data_hdr_write(*args, **kwargs):
  """  Write data information to disk  
    FORMAT V = spm_data_hdr_write(V)  
    V        - a structure array (see spm_data_hdr_read)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_data_hdr_write.m)
  """

  return Runtime.call("spm_data_hdr_write", *args, **kwargs)
