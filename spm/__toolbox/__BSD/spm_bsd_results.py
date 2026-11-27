from spm._runtime import Runtime


def spm_bsd_results(*args, **kwargs):
    r"""
      spm_bsd_results - Processes BSD results and optionally displays figures.  
         
        Syntax:  
          spm_bsd_results(BSD, fignum)  
         
        Inputs:  
          BSD    - Structure containing BSD analysis results.  
          fignum - (Optional) Figure number for result visualization.  
         
        Description:  
          This function processes the results contained in the BSD structure,  
          performing necessary computations and optionally displaying results  
          in the specified figure window.  
       _______________________________________________________________________  
        Copyright (C) 2024-2025 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/BSD/spm_bsd_results.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bsd_results", *args, **kwargs, nargout=0)
