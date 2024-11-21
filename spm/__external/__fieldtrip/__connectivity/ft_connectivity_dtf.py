from spm.__wrapper__ import Runtime


def ft_connectivity_dtf(*args, **kwargs):
    """
      FT_CONNECTIVITY_DTF computes the directed transfer function.  
         
        Use as  
          [d, v, n] = ft_connectivity_dtf(inputdata, ...)  
         
        The input should be a spectral transfer matrix organized as  
          Nrpt x Nchan x Nchan x Nfreq (x Ntime)  
        where Nrpt can be 1.  
         
        The output represents  
          d = partial directed coherence matrix Nchan x Nchan x Nfreq (x Ntime).  
              If multiple observations in the input, the average is returned.  
          v = variance of d across observations.  
          n = number of observations.  
         
        Typically, nrpt should be 1 where the spectral transfer matrix is computed across  
        observations. When nrpt>1 and hasjack=true, the input is assumed to contain the  
        leave-one-out estimates of the spectral transfer matrix, thus a more reliable  
        estimate of the relevant quantities.  
         
        Additional optional input arguments come as key-value pairs:  
          'hasjack'   = boolean, specifying whether the input contains leave-one-outs,  
                        required for correct variance estimate (default = false)  
          'crsspctrm' = matrix containing the cross-spectral density. If this  
                        matrix is defined, the function returns the ddtf, which  
                        requires an estimation of partial coherence from this matrix.  
          'invfun'    = 'inv' (default) or 'pinv', the function used to invert the  
                        crsspctrm matrix to obtain the partial coherence. Pinv is  
                        useful if the data are poorly-conditioned.  
          'feedback'  = 'none', 'text', 'textbar', 'dial', 'etf', 'gui' type of feedback showing progress of computation, see FT_PROGRESS  
         
        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/ft_connectivity_dtf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_connectivity_dtf", *args, **kwargs)
