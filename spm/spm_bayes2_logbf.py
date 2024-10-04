from spm.__wrap__ import _Runtime


def spm_bayes2_logbf(*args, **kwargs):
  """  Compute and write log Bayes factor image  
    FORMAT [xCon,SPM]= spm_bayes2_logbf(SPM,XYZ,xCon,ic)  
     
    SPM  - SPM data structure  
    XYZ  - voxel list  
    xCon - contrast info  
    ic   - contrast number  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_bayes2_logbf.m)
  """

  return _Runtime.call("spm_bayes2_logbf", *args, **kwargs)
