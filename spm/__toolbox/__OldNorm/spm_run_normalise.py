from spm.__wrapper__ import Runtime


def spm_run_normalise(*args, **kwargs):
    """
      SPM job execution function  
        takes a harvested job data structure and call SPM functions to perform  
        computations on the data.  
        Input:  
        job    - harvested job data structure (see matlabbatch help)  
        Output:  
        out    - computation results, usually a struct variable.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/OldNorm/spm_run_normalise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_run_normalise", *args, **kwargs)
