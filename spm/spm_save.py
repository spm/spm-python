from spm.__wrapper__ import Runtime


def spm_save(*args, **kwargs):
  """  Save text and numeric data to file  
    FORMAT spm_save(f,var,opts,...)  
    f     - filename (can be gzipped) {csv,tsv,json,txt,mat,npy}  
    var   - data array or structure  
    opts  - optional inputs to be passed on to lower level function  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_save.m)
  """

  return Runtime.call("spm_save", *args, **kwargs, nargout=0)
