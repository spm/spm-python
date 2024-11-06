from spm.__wrapper__ import Runtime


def spm_vec(*args, **kwargs):
    """
      Vectorise a numeric, cell or structure array - a compiled routine  
        FORMAT [vX] = spm_vec(X)  
        X  - numeric, cell or structure array[s]  
        vX - vec(X)  
         
        See spm_unvec  
       __________________________________________________________________________  
         
        e.g.:  
        spm_vec({eye(2) 3}) = [1 0 0 1 3]'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vec.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vec", *args, **kwargs)
