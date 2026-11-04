from spm._runtime import Runtime


def spm_design_factorial(*args, **kwargs):
    r"""
      Extract factorial matrix, file list and H partition of design matrix  
        FORMAT [I,P,H,Hnames] = spm_design_factorial(fd)  
         
        fd       - structure defined in spm_cfg_factorial_design  
                   with fields fact and icell  
         
        I        - Nscan x 4 factor matrix  
        P        - List of scans  
        H        - Component of design matrix describing conditions  
        Hnames   - Condition names  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_design_factorial.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_design_factorial", *args, **kwargs)
