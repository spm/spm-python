from spm._runtime import Runtime


def spm_design_flexible(*args, **kwargs):
    r"""
      Create H partition of design matrix  
        FORMAT [H,Hnames,B,Bnames] = spm_design_flexible(fblock,I)  
         
        fblock   - Part of job structure containing within-subject design info  
        I        - Nscan x 4 factor matrix  
         
        H        - Component of design matrix describing conditions  
        Hnames   - Condition names  
        B        - Component of design matrix describing blocks  
        Bnames   - Block names  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_design_flexible.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_design_flexible", *args, **kwargs)
