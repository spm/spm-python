from spm.__wrapper__ import Runtime


def bf_features_vbfa(*args, **kwargs):
    """
      Variational Bayes Factor Analysis for computing noise covariance  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_vbfa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_features_vbfa", *args, **kwargs)
