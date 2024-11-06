from spm.__wrapper__ import Runtime


def spm_design_within_subject(*args, **kwargs):
    """
      Set up within-subject design when specified subject by subject  
        FORMAT [I,P,cov] = spm_design_within_subject(fblock,cov)  
         
        fblock   - Part of job structure containing within-subject design info  
        cov      - Part of job structure containing covariate info  
         
        I        - Nscan x 4 factor matrix  
        P        - List of scans  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_design_within_subject.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_design_within_subject", *args, **kwargs)
