from spm._runtime import Runtime


def spm_tile(*args, **kwargs):
    r"""
      Grouping into a partition of non-overlapping outcome tiles  
        FORMAT [G,M,H] = spm_tile(L,d)  
       --------------------------------------------------------------------------  
        L  - locations  
        d  - size (diameter) of tile in pixels  
         
        G  - cell array of outcome indices  
        M  - and their locations  
        H  - cell array of weights (c.f., receptive field)  
         
        This routine identifies overlapping groups of pixels, returning their  
        mean locations and a cell array of weights (based upon radial Gaussian  
        basis functions) for each group. In other words, the grouping is based  
        upon the location of pixels; in the spirit of a receptive field afforded  
        by a sensory epithelium.Effectively, this leverages the conditional  
        independencies that inherit from local interactions; of the kind found in  
        metric spaces that preclude action at a distance.  
       --------------------------------------------------------------------------  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_tile.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_tile", *args, **kwargs)
