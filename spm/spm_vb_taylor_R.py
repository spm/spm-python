from spm.__wrapper__ import Runtime


def spm_vb_taylor_R(*args, **kwargs):
    """
      Get Taylor series approximation to posterior correlation matrices  
        FORMAT [slice] = spm_vb_taylor_R(Y,slice)  
         
        Y        - data  
        slice    - VB-GLMAR data structure  
         
        See paper VB3.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_taylor_R.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_taylor_R", *args, **kwargs)
