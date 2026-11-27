from spm._runtime import Runtime


def _standardise(*args, **kwargs):
    r"""
      STANDARDISE computes the zscore of a matrix along dimension dim  
        has similar functionality as the stats-toolbox's zscore function  
         
        Use as  
          x = standardise(x, dim)  
         
        See also ZSCORE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/standardise.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("standardise", *args, **kwargs)
