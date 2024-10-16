from spm.__wrapper__ import Runtime


def spm_read_hdr(*args, **kwargs):
  """  Read (SPM customised) Analyze header  
    FORMAT [hdr,otherendian] = spm_read_hdr(fname)  
    fname       - .hdr filename  
    hdr         - structure containing Analyze header  
    otherendian - byte swapping necessary flag  
   _______________________________________________________________________  
    Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/compat/spm_read_hdr.m)
  """

  return Runtime.call("spm_read_hdr", *args, **kwargs)
