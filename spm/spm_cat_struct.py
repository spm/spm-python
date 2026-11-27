from spm._runtime import Runtime


def spm_cat_struct(*args, **kwargs):
    r"""
      Concatenates structure arrays with possibly different fields  
        FORMAT s = spm_cat_struct(s1, s2, ...)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_cat_struct.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cat_struct", *args, **kwargs)
