from spm.__wrap__ import _Runtime


def spm_prep2sn(*args, **kwargs):
  """  Convert the output from spm_preproc into an sn.mat file  
    FORMAT [po,pin] = spm_prep2sn(p)  
    p   - the results of spm_preproc  
     
    po  - the output in a form that can be used by spm_write_sn  
    pin - the inverse transform in a form that can be used by spm_write_sn  
     
    The outputs are saved in sn.mat files only if they are not requested LHS.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/OldSeg/spm_prep2sn.m)
  """

  return _Runtime.call("spm_prep2sn", *args, **kwargs)
