from spm.__wrap__ import _Runtime


def spm_dcm_csd_source_optimise(*args, **kwargs):
  """  Stochastic optimisation of single source neural mass model  
    FORMAT [PE] = spm_dcm_csd_source_optimise  
     
    Edit the set up variable in the main body of this routine to specify   
    desired frequency responses (in selected populations)  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_csd_source_optimise.m)
  """

  return _Runtime.call("spm_dcm_csd_source_optimise", *args, **kwargs)
