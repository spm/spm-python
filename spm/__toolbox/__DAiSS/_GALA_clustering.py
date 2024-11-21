from spm.__wrapper__ import Runtime


def _GALA_clustering(*args, **kwargs):
    """
    GALA_clustering is a function.  
          res = GALA_clustering(lJcov, J1, S, distance, A)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/GALA_clustering.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("GALA_clustering", *args, **kwargs)
