from spm.__wrapper__ import Runtime


def spm_check_orientations(*args, **kwargs):
    """
      Check the dimensions and orientations of the images  
        FORMAT [sts, str] = spm_check_orientations(V [,verbose])  
        V       - a struct array as returned by spm_vol  
        verbose - [Default: true]  
         
        sts     - status (true means OK)  
        str     - string describing status, empty if OK  
         
        When used without LHS, this function throws an error accordingly.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_check_orientations.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_check_orientations", *args, **kwargs)
