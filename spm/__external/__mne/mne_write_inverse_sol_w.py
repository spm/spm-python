from spm.__wrapper__ import Runtime


def mne_write_inverse_sol_w(*args, **kwargs):
    """
       
        function mne_write_inverse_sol_w(stem,inv,sol)  
         
        Save static inverse solution data into stc files  
         
        stem      - Stem for the w files  
        inv       - The inverse operator structure (can be the forward operator as well)  
        sol       - The solution matrix (number of locations)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_write_inverse_sol_w.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_write_inverse_sol_w", *args, **kwargs, nargout=0)
