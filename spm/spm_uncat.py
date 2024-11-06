from spm.__wrapper__ import Runtime


def spm_uncat(*args, **kwargs):
    """
      Convert a matrix into an array  
        FORMAT [a] = spm_uncat(x,a)  
        x - matrix  
        a - cell array  
         
        i.e. a = spm_uncat(spm_cat(a),a)  
         
        see also spm_vec and spm_unvec  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_uncat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_uncat", *args, **kwargs)
