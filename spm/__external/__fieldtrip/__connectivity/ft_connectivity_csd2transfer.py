from spm.__wrapper__ import Runtime


def ft_connectivity_csd2transfer(*args, **kwargs):
    """
      FT_CONNECTIVITY_CSD2TRANSFER computes the transfer-function from frequency domain  
        data using the Wilson-Burg algorithm. The transfer function can be used for the  
        computation of directional measures of connectivity, such as Granger causality,  
        partial directed coherence, or directed transfer functions.  
         
        Use as  
          [output] = ft_connectivity_csd2transfer(freq, ...)  
         
        The input variable freq should be a FieldTrip data structure containing frequency  
        domain data containing the cross-spectral density computed between all pairs of  
        channels, thus containing a 'dimord' of 'chan_chan_freq(_time)'.  
         
        Additional optional input arguments come as key-value pairs:  
          numiteration = scalar value (default: 100) the number of iterations  
          channelcmb   = Nx2 cell-array listing the channel pairs for the spectral  
                           factorization. If not defined or empty (default), a  
                           full multivariate factorization is performed, otherwise  
                           a multiple pairwise factorization is done.  
          tol          = scalar value (default: 1e-18) tolerance limit truncating  
                           the iterations  
          sfmethod     = 'multivariate', or 'bivariate'  
          stabilityfix = false, or true. zigzag-reduction by means of tapering of the  
                           intermediate time domain representation when computing the  
                           plusoperator  
         
        The code for the Wilson-Burg algorithm has been very generously provided by Dr.  
        Mukesh Dhamala, and Prof. Mingzhou Ding and his group, and has been adjusted for  
        efficiency. If you use this code for studying directed interactions, please cite  
        the following references:  
          - M.Dhamala, R.Rangarajan, M.Ding, Physical Review Letters 100, 018701 (2008).  
          - M.Dhamala, R.Rangarajan, M.Ding, Neuroimage 41, 354 (2008).  
         
        See also FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/ft_connectivity_csd2transfer.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_connectivity_csd2transfer", *args, **kwargs)
