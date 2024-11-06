from spm.__wrapper__ import Runtime


def ft_connectivity_cancorr(*args, **kwargs):
    """
      FT_CONNECTIVITY_CANCORR computes the canonical correlation or canonical coherence  
        between multiple variables. Canonical correlation analysis (CCA) is a way of  
        measuring the linear relationship between two multidimensional variables. It finds  
        two bases, one for each variable, that are optimal with respect to correlations  
        and, at the same time, it finds the corresponding correlations.  
         
        Use as  
          [R] = ft_connectivity_cancorr(inputdata, ...)  
         
        The input data should be a covariance or cross-spectral density array organized as  
          Channel x Channel  
        or  
          Channel x Channel (x Frequency)  
         
        The output R represents the max(indices)*max(indices) canonical correlation matrix  
        or canonical coherence matrix.  
         
        Additional optional input arguments come as key-value pairs:  
          'indices'  = 1xNchan vector with indices of the groups to which the channels belong,  
                       e.g. [1 1 2 2] for a 2-by-2 connectivity between 2 planar MEG channels  
          'realflag' = boolean flag whether to use the real-valued part only for the determination  
                       of the rotation (default = false)  
         
        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/ft_connectivity_cancorr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_connectivity_cancorr", *args, **kwargs)
