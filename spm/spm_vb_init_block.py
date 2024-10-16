from spm.__wrapper__ import Runtime


def spm_vb_init_block(*args, **kwargs):
  """  Initialise Variational Bayes for GLM-AR models  
    FORMAT [block] = spm_vb_init_block(Y,block)  
     
    Y      - [T x N] time series with T time points, N voxels  
    block  - data structure (see spm_vb_glmar)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vb_init_block.m)
  """

  return Runtime.call("spm_vb_init_block", *args, **kwargs)
