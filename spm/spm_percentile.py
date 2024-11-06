from spm.__wrapper__ import Runtime


def spm_percentile(*args, **kwargs):
    """
      Compute one or more percentiles from data  
        FORMAT [y] = spm_percentile(data, p)  
        data - arbitrarily sized input data (from which NaNs will be excluded)  
        p    - scalar or n-vector of percentage values (from 0 to 100)  
               if not specified, p defaults to all quartiles: [0 25 50 75 100]  
         
        y    - scalar or n-vector of corresponding percentiles  
         
        Note that percentiles are computed over all data, not along the first or  
        specified dimension (unlike prctile from the MATLAB Statistics Toolbox).  
         
        Example:  
         spm_summarise(vols, 'all', @spm_percentile) % quartiles of images  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_percentile.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_percentile", *args, **kwargs)
