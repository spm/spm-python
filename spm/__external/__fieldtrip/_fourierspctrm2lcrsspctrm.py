from spm.__wrapper__ import Runtime


def _fourierspctrm2lcrsspctrm(*args, **kwargs):
    """
      FOURIERSPCTRM2LCRSSPCTRM is a helper function that converts the input fourierspctrm  
        into a lagged crsspctrm, to enable computation of lagged coherence as described in  
        the publication referenced below. It is used in ft_connectivityanalysis in order to  
        reorganize the input data.  
         
        The input data should be organised in a structure as obtained from the  
        FT_FREQANALYSIS function (freq), such that freq contains the fields 'fourierspctrm'  
        and 'time'. The timepoints must be chosen such that the desired cfg.lag/cfg.foi  
        (lag in seconds) is an integer multiple of the time resolution in freq.  
         
        Options come in key-value pairs, and may contain  
          lag = scalar (or vector) of time shifts, expressed in units of time  
             We recommend users to choose cfg.lag such that it is larger or equal  
             to the width of the wavelet used for each Fourier transform in ft_freqanalysis  
          timeresolved = 'yes' or 'no' (default='no'). If set to yes, lagged  
             coherence is calculated separately for each pair of timepoints that  
             is separated by lag  
          channelcmb   =  Mx2 cell-array with selection of channel pairs,  
             see ft_channelcombination, default = {'all' 'all'};  
         
        When this measure is used for your publication, please cite:  
          Fransen, Anne M. M, Van Ede, Freek, Maris, Eric (2015) Identifying  
          oscillations on the basis of rhythmicity. NeuroImage 118: 256-267.  
        You may also want to acknowledge the fact that J.M. Schoffelen has  
        written the actual implementation.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/fourierspctrm2lcrsspctrm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fourierspctrm2lcrsspctrm", *args, **kwargs)
