from spm._runtime import Runtime


def mne_write_inverse_sol_w(*args, **kwargs):
    r"""
       
        function mne_write_inverse_sol_w(stem,inv,sol)  
         
        Save static inverse solution data into stc files  
         
        stem      - Stem for the w files  
        inv       - The inverse operator structure (can be the forward operator as well)  
        sol       - The solution matrix (number of locations)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_write_inverse_sol_w.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_write_inverse_sol_w", *args, **kwargs, nargout=0)
