from spm.__wrapper__ import Runtime


def spm_length(*args, **kwargs):
    """
      Length of a vectorised numeric, cell or structure array  
        FORMAT [n] = spm_length(X)  
        X    - numeric, cell or structure array[s]  
        n    - length(spm_vec(X))  
         
        See spm_vec, spm_unvec  
       __________________________________________________________________________  
         
        e.g.:  
        spm_length({eye(2) 3}) = 5  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_length.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_length", *args, **kwargs)
