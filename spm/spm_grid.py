from spm._runtime import Runtime


def spm_grid(*args, **kwargs):
    r"""
      Superimpose a Talairach and Tournoux grid  
        FORMAT O = spm_grid(I)  
        I - image matrix  
        O - image matrix with grid added  
       __________________________________________________________________________  
         
        spm_grid adds a grid to the input argument.  
        The grid is scaled to 10% of the input's maximum.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_grid.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_grid", *args, **kwargs)
