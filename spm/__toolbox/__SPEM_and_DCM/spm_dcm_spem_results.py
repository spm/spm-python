from spm._runtime import Runtime


def spm_dcm_spem_results(*args, **kwargs):
    r"""
      Display (DCM results of) of smooth pursuit eye movements  
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/SPEM_and_DCM/spm_dcm_spem_results.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_spem_results", *args, **kwargs)
