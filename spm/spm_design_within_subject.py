from spm._runtime import Runtime


def spm_design_within_subject(*args, **kwargs):
    r"""
      Set up within-subject design when specified subject by subject  
        FORMAT [I,P,cov] = spm_design_within_subject(fblock,cov)  
         
        fblock   - Part of job structure containing within-subject design info  
        cov      - Part of job structure containing covariate info  
         
        I        - Nscan x 4 factor matrix  
        P        - List of scans  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_design_within_subject.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_design_within_subject", *args, **kwargs)
