from spm.__wrap__ import _Runtime


def spm_dcm_spem_results(*args, **kwargs):
  """  Display (DCM results of) of smooth pursuit eye movements  
    FORMAT DCM = spm_dcm_spem_results(DCM)  
     
    DCM  
        name: name string  
          xY: data   [1x1 struct]  
          xU: design [1x1 struct]  
          pE: prior expectation  
          pC: prior covariance  
     
    and (if inverted)  
     
          Y{i}   - predicted responses  
          DEM{i} - ADEM inversion structure  
          Ep     - posterior expectation  
          Cp     - posterior covariance  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/SPEM_and_DCM/spm_dcm_spem_results.m)
  """

  return _Runtime.call("spm_dcm_spem_results", *args, **kwargs)
