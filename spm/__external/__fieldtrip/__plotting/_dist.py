from spm._runtime import Runtime


def _dist(*args, **kwargs):
    r"""
      DIST computes the euclidean distance between the columns of the input matrix  
         
        Use as  
          [d] = dist(x)  
        where x is for example an 3xN matrix with positions in 3D space.  
         
        This function serves as a replacement for the dist function in the Neural  
        Networks toolbox.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/dist.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dist", *args, **kwargs)
