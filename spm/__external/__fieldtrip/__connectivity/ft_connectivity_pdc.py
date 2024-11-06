from spm.__wrapper__ import Runtime


def ft_connectivity_pdc(*args, **kwargs):
    """
      FT_CONNECTIVITY_PDC computes partial directed coherence. This function implements  
        the metrices described in Baccala et al., Biological Cybernetics 2001, 84(6),  
        463-74. and in Baccala et al., 15th Int.Conf.on DSP 2007, 163-66.  
         
        The implemented algorithm has been tested against the implementation in the  
        SIFT-toolbox. It yields numerically identical results to what is known there as  
        'nPDC' (for PDC) and 'GPDC' for generalized pdc.  
         
        Use as  
          [p, v, n] = ft_connectivity_pdc(inputdata, ...)  
         
        The input data should be a spectral transfer matrix organized as  
          Nrpt x Nchan x Nchan x Nfreq (x Ntime),  
        where Nrpt can be 1.  
         
        Additional optional input arguments come as key-value pairs:  
          'hasjack'   = 0 (default) is a boolean specifying whether the input  
                        contains leave-one-outs, required for correct variance  
                        estimate  
          'invfun'    = 'inv' (default) or 'pinv', the function used to invert the  
                        transfer matrix to obtain the fourier transform of the  
                        MVAR coefficients. Use 'pinv' if the data are  
                        poorly-conditioned.  
          'noisecov'  = matrix containing the covariance of the residuals of the  
                        MVAR model. If this matrix is defined, the function  
                        returns the generalized partial directed coherence.  
          'feedback'  = 'none', 'text', 'textbar', 'dial', 'etf', 'gui' type of feedback showing progress of computation, see FT_PROGRESS  
         
        Output arguments:  
          p = partial directed coherence matrix Nchan x Nchan x Nfreq (x Ntime).  
              If multiple observations in the input, the average is returned.  
          v = variance of p across observations.  
          n = number of observations.  
         
        Typically, nrpt should be 1 (where the spectral transfer matrix is  
        computed across observations. When nrpt>1 and hasjack is true the input  
        is assumed to contain the leave-one-out estimates of H, thus a more  
        reliable estimate of the relevant quantities.  
         
        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/ft_connectivity_pdc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_connectivity_pdc", *args, **kwargs)
