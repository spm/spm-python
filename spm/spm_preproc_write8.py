from spm.__wrapper__ import Runtime


def spm_preproc_write8(*args, **kwargs):
  """  Write out VBM preprocessed data  
    FORMAT [cls,M1] = spm_preproc_write8(res,tc,bf,df,mrf,cleanup,bb,vx,odir)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_preproc_write8.m)
  """

  return Runtime.call("spm_preproc_write8", *args, **kwargs)
