from spm._runtime import Runtime


def spm_eeg_invert_bma(*args, **kwargs):
    r"""
      Compute Bayesian Model Average given a set of current distributions and model evidences  
        FORMAT [Jbma,qCbma,PostMax]=spm_eeg_invert_bma(manyinverse,F)  
         
        At the moment makes an estimate of posterior covariance based on relative  
        weighting of the input posteriors but this could be changed in future.  
        At the moment adds a random DC offset (and not a random time series) to  
        the estimated current distribution at each vertex.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_invert_bma.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_invert_bma", *args, **kwargs)
