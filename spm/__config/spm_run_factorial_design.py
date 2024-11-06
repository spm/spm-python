from spm.__wrapper__ import Runtime


def spm_run_factorial_design(*args, **kwargs):
    """
      SPM job execution function - factorial design specification  
        Input:  
        job    - harvested job data structure (see matlabbatch help)  
        Output:  
        out    - struct variable containing the path of the saved SPM.mat  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_run_factorial_design.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_run_factorial_design", *args, **kwargs)
