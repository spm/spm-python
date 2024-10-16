from spm.__wrapper__ import Runtime


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

  return Runtime.call("spm_bayes2_logbf", *args, **kwargs)
