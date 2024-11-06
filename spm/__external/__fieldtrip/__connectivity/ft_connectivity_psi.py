from spm.__wrapper__ import Runtime


def ft_connectivity_psi(*args, **kwargs):
    """
      FT_CONNECTIVITY_PSI computes the phase slope index from a data-matrix containing  
        the cross-spectral density. This implements the method described in Nolte et al.,  
        Robustly estimating the flow direction of information in complex physical systems.  
        Physical Review Letters, 2008; 100; 234101.  
         
        Use as  
          [c, v, n] = ft_connectivity_psi(inputdata, ...)  
         
        Where the input data input should be organized as  
          Repetitions x Channel x Channel (x Frequency) (x Time)  
        or  
          Repetitions x Channelcombination (x Frequency) (x Time)  
         
        The first dimension should be singleton if the input already contains an  
        average.  
         
        The output p contains the phase slope index, v is a variance estimate which only  
        can be computed if the data contains leave-one-out samples, and n is the number of  
        repetitions in the input data. If the phase slope index is positive, then the first  
        chan (1st dim) becomes more leading (or less lagged) with higher frequency,  
        indicating that it is causally driving the second channel (2nd dim).  
         
        Additional optional input arguments come as key-value pairs:  
          'nbin'			=	scalar, half-bandwidth parameter: the number of frequency bins across which to integrate  
          'hasjack'		= boolean, specifying whether the repetitions represent leave-one-out samples (allowing for a variance estimate)  
          'feedback'  = 'none', 'text', 'textbar', 'dial', 'etf', 'gui' type of feedback showing progress of computation, see FT_PROGRESS  
          'dimord'		= string, specifying how the input matrix should be interpreted  
          'powindx'   = ?  
          'normalize' = ?  
         
        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/ft_connectivity_psi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_connectivity_psi", *args, **kwargs)
