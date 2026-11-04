from spm._runtime import Runtime


def spm_dcm_contrasts(*args, **kwargs):
    r"""
      Make contrast vector for a DCM  
        FORMAT con = spm_dcm_contrasts(DCM,D)  
         
        DCM    - DCM structure or its filename  
        D      - 'A','B' or 'C' i.e. connectivity matrix of interest  
         
        con    - column vector specifying contrast weights  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_contrasts.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_contrasts", *args, **kwargs)
