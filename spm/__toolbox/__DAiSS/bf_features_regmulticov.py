from spm.__wrapper__ import Runtime


def bf_features_regmulticov(*args, **kwargs):
    """
      Simple covariance computation with regularization  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_regmulticov.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_features_regmulticov", *args, **kwargs)
