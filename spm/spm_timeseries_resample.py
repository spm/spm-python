from spm.__wrapper__ import Runtime


def spm_timeseries_resample(*args, **kwargs):
    """
      Basic resample function (when no Signal Proc. Toolbox)  
        FORMAT [Y,alpha] = spm_timeseries_resample(X,alpha)  
        X      - (n x m) matrix of n time series of length m  
        alpha  - the ratio of input versus output sampling frequencies.  
                 If alpha>1, this performs upsampling of the time series.  
         
        Y      - (n x [alpha*m]) matrix of resampled time series  
        alpha  - true alpha used (due to rational rounding)  
         
        This function operates on rows of a signal matrix.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_timeseries_resample.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_timeseries_resample", *args, **kwargs)
