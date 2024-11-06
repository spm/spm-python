from spm.__wrapper__ import Runtime


def spm_run_bms_vis(*args, **kwargs):
    """
      Show results for Bayesian Model Selection Maps  
        SPM job execution function  
        takes a harvested job data structure (or no input) and calls SPM   
        functions to show results from Bayesian Model Selection of   
        Log. Evidence Maps    
         
        Input:  
        Varargin - can be harvested job data structure (see matlabbatch help).  
        Output:  
        No output.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_run_bms_vis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_run_bms_vis", *args, **kwargs, nargout=0)
