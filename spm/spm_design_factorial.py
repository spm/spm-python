from spm.__wrapper__ import Runtime


def spm_design_factorial(*args, **kwargs):
    """
      Extract factorial matrix, file list and H partition of design matrix  
        FORMAT [I,P,H,Hnames] = spm_design_factorial(fd)  
         
        fd       - structure defined in spm_cfg_factorial_design  
                   with fields fact and icell  
         
        I        - Nscan x 4 factor matrix  
        P        - List of scans  
        H        - Component of design matrix describing conditions  
        Hnames   - Condition names  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_design_factorial.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_design_factorial", *args, **kwargs)
