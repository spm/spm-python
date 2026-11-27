from spm._runtime import Runtime


def spm_check_orientations(*args, **kwargs):
    r"""
      Check the dimensions and orientations of the images  
        FORMAT [sts, str] = spm_check_orientations(V [,verbose])  
        V       - a struct array as returned by spm_vol  
        verbose - [Default: true]  
         
        sts     - status (true means OK)  
        str     - string describing status, empty if OK  
         
        When used without LHS, this function throws an error accordingly.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_check_orientations.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_check_orientations", *args, **kwargs)
