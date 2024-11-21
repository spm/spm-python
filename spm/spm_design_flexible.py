from spm.__wrapper__ import Runtime


def spm_design_flexible(*args, **kwargs):
    """
      Create H partition of design matrix  
        FORMAT [H,Hnames,B,Bnames] = spm_design_flexible(fblock,I)  
         
        fblock   - Part of job structure containing within-subject design info  
        I        - Nscan x 4 factor matrix  
         
        H        - Component of design matrix describing conditions  
        Hnames   - Condition names  
        B        - Component of design matrix describing blocks  
        Bnames   - Block names  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_design_flexible.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_design_flexible", *args, **kwargs)
