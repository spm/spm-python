from spm._runtime import Runtime


def spm_run_bms_vis(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_run_bms_vis.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_run_bms_vis", *args, **kwargs, nargout=0)
