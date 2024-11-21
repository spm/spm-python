from spm.__wrapper__ import Runtime


def spm_cat_struct(*args, **kwargs):
    """
      Concatenates structure arrays with possibly different fields  
        FORMAT s = spm_cat_struct(s1, s2, ...)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_cat_struct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cat_struct", *args, **kwargs)
