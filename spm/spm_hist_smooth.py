from spm.__wrapper__ import Runtime


def spm_hist_smooth(*args, **kwargs):
    """
      Histogram smoothing (graph Laplacian)  
        FORMAT x = spm_hist_smooth(x,s)  
        x   - data vector  
        s   - smoothing  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_hist_smooth.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_hist_smooth", *args, **kwargs)
