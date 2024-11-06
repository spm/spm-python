from spm.__wrapper__ import Runtime


def mne_write_inverse_sol_stc(*args, **kwargs):
    """
       
        function mne_write_inverse_sol_stc(stem,inv,sol,tmin,tstep)  
         
        Save dynamic inverse solution data into stc files  
         
        stem      - Stem for the stc files  
        inv       - The inverse operator structure (can be the forward operator as well)  
        sol       - A solution matrix (locations x time)  
        tmin      - Time of the first data point in seconds  
        tstep     - Time between data points in seconds  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_write_inverse_sol_stc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_write_inverse_sol_stc", *args, **kwargs, nargout=0)
