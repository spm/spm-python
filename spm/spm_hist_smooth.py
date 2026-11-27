from spm._runtime import Runtime


def spm_hist_smooth(*args, **kwargs):
    r"""
      Histogram smoothing (graph Laplacian)  
        FORMAT x = spm_hist_smooth(x,s)  
        x   - data vector  
        s   - smoothing  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_hist_smooth.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_hist_smooth", *args, **kwargs)
