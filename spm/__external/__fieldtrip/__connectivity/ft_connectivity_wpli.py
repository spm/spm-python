from spm.__wrapper__ import Runtime


def ft_connectivity_wpli(*args, **kwargs):
    """
      FT_CONNECTIVITY_WPLI computes the weighted phase lag index from a data matrix  
        containing the cross-spectral density. This implements the method described in  
        Vinck M, Oostenveld R, van Wingerden M, Battaglia F, Pennartz CM. An improved index  
        of phase-synchronization for electrophysiological data in the presence of  
        volume-conduction, noise and sample-size bias. Neuroimage. 2011 Apr  
        15;55(4):1548-65.  
         
        Use as  
          [wpi, v, n] = ft_connectivity_wpli(inputdata, ...)  
         
        The input data input should contain cross-spectral densities organized as:  
          Repetitions x Channel x Channel (x Frequency) (x Time)  
        or  
          Repetitions x Channelcombination (x Frequency) (x Time)  
          
        Alternatively, the input data can contain fourier coefficients organized  
        as:  
          Repetitions_tapers x Channel (x Frequency) (x Time)   
         
        The first dimension of the input data matrix should contain repetitions and should not   
        contain an average already. Also, the input should not consist of leave-one-out averages.  
         
        The output wpli contains the wpli, v is a leave-one-out variance estimate  
        which is only computed if dojack=true, and n is the number of repetitions  
        in the input data.  
         
        Additional optional input arguments come as key-value pairs:  
          'dojack'    = boolean, compute a variance estimate based on  
                        leave-one-out, only supported when input data is a  
                        bivariate cross-spectral density  
          'debias'    = boolean, compute debiased wpli or not  
          'feedback'  = 'none', 'text', 'textbar', 'dial', 'etf', 'gui' type of feedback   
                        showing progress of computation, see FT_PROGRESS  
          'isunivariate' = boolean, compute CSD on fly (saves memory with many trials)  
          'cumtapcnt' = vector that contains the cumulative taper counter, defining how  
                        tapers should be combined to define repetitions. If not  
                        defined (or empty), it will be ones(size(input,1),1),  
                        i.e. each slice of the matrix is considered a repetition.  
                        This option is only function in case isunivariate = true  
         
        See also FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/ft_connectivity_wpli.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_connectivity_wpli", *args, **kwargs)
