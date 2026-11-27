from spm._runtime import Runtime


def pdist2(*args, **kwargs):
    r"""
      PDIST2 computes the distance between all points in input matrix X and Y.  
         
        Use as  
          d = pdist(x, y)  
         
        The output is a matrix with size MX x MY.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/stats/pdist2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("pdist2", *args, **kwargs)
