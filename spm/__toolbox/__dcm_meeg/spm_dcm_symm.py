from spm._runtime import Runtime


def spm_dcm_symm(*args, **kwargs):
    r"""
      Lock ECD orientations by introducing prior correlations  
        FORMAT [pC] = spm_dcm_symm(pV,pE)  
       __________________________________________________________________________  
         
        pE   - prior expectation  
        pV   - prior variance  
        pC   - prior covariance  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_dcm_symm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_symm", *args, **kwargs)
