from spm.__wrapper__ import Runtime


def spm_filter(*args, **kwargs):
    """
      Removes low frequency confounds X0  
        FORMAT [Y] = spm_filter(K,Y)  
        FORMAT [K] = spm_filter(K)  
         
        K           - filter matrix or:  
        K(s)        - struct array containing partition-specific specifications  
         
        K(s).RT     - observation interval in seconds  
        K(s).row    - row of Y constituting block/partition s  
        K(s).HParam - cut-off period in seconds  
         
        K(s).X0     - low frequencies to be removed (DCT)  
         
        Y           - data matrix  
         
        K           - filter structure  
        Y           - filtered data  
       __________________________________________________________________________  
         
        spm_filter implements high-pass filtering in an efficient way by  
        using the residual forming matrix of X0 - low frequency confounds.  
        spm_filter also configures the filter structure in accord with the  
        specification fields if called with one argument.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_filter.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_filter", *args, **kwargs)
