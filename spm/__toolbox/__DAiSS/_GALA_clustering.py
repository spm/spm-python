from spm._runtime import Runtime


def _GALA_clustering(*args, **kwargs):
    r"""
    GALA_clustering is a function.  
          res = GALA_clustering(lJcov, J1, S, distance, A)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/private/GALA_clustering.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("GALA_clustering", *args, **kwargs)
