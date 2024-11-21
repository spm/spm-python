from spm.__wrapper__ import Runtime


def ft_timelocksimulation(*args, **kwargs):
    """
      FT_TIMELOCKSIMULATION computes simulated data that consists of multiple trials in  
        with each trial contains an event-related potential or field. Following  
        construction of the time-locked signal in each trial by this function, the signals  
        can be passed into FT_TIMELOCKANALYSIS to obtain the average and the variance.  
         
        Use as  
          [data] = ft_timelockstatistics(cfg)  
        which will return a raw data structure that resembles the output of  
        FT_PREPROCESSING.  
         
        The number of trials and the time axes of the trials can be specified by  
          cfg.fsample    = simulated sample frequency (default = 1000)  
          cfg.trllen     = length of simulated trials in seconds (default = 1)  
          cfg.numtrl     = number of simulated trials (default = 10)  
          cfg.baseline   = number (default = 0.3)  
        or by  
          cfg.time       = cell-array with one time axis per trial, which are for example obtained from an existing dataset  
         
        The signal is constructed from three underlying functions. The shape is  
        controlled with  
          cfg.s1.numcycli = number (default = 1)  
          cfg.s1.ampl     = number (default = 1.0)  
          cfg.s2.numcycli = number (default = 2)  
          cfg.s2.ampl     = number (default = 0.7)  
          cfg.s3.numcycli = number (default = 4)  
          cfg.s3.ampl     = number (default = 0.2)  
          cfg.noise.ampl  = number (default = 0.1)  
        Specifying numcycli=1 results in a monophasic signal, numcycli=2 is a biphasic,  
        etc. The three signals are scaled to the indicated amplitude, summed up and a  
        certain amount of noise is added.  
         
        Other configuration options include  
          cfg.numchan    = number (default = 5)  
          cfg.randomseed = 'yes' or a number or vector with the seed value (default = 'yes')  
         
        See also FT_TIMELOCKANALYSIS, FT_TIMELOCKSTATISTICS, FT_FREQSIMULATION,  
        FT_DIPOLESIMULATION, FT_CONNECTIVITYSIMULATION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_timelocksimulation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_timelocksimulation", *args, **kwargs)
