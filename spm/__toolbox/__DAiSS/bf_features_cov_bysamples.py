from spm.__wrapper__ import Runtime


def bf_features_cov_bysamples(*args, **kwargs):
    """
      Simple covariance computation to handle variable width WOIs,   
        Requires S.samples as a [1 x samples x ntrials] matrix of logical indices  
        indicating which data points should be used in the cov estimation  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_cov_bysamples.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_features_cov_bysamples", *args, **kwargs)
