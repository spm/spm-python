from spm.__wrapper__ import Runtime


def ft_statfun_bayesfactor(*args, **kwargs):
    """
      FT_STATFUN_BAYESFACTOR computes the Bayes factor for a H0 of the data in two  
        conditions having the same mean, versus H1 of the data having different means. This  
        function supports both unpaired and paired designs and assumes flat priors.  
         
        Lee and Wagenmakers (2013) provide these guidelines for its interpretation  
          IF B10 IS...    THEN YOU HAVE...  
            > 100           Extreme evidence for H1  
            30 – 100        Very strong evidence for H1  
            10 – 30         Strong evidence for H1  
            3 – 10          Moderate evidence for H1  
            1 – 3           Anecdotal evidence for H1  
            1               No evidence  
            1/3 – 1         Anecdotal evidence for H0  
            1/3 – 1/10      Moderate evidence for H0  
            1/10 – 1/30     Strong evidence for H0  
            1/30 – 1/100    Very strong evidence for H0  
            < 1/100         Extreme evidence for H0  
         
        Use this function by calling one of the high-level statistics functions as  
          [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)  
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)  
          [stat] = ft_sourcestatistics(cfg, source1, source2, ...)  
        with the following configuration option:  
          cfg.statistic = 'ft_statfun_bayesfactor'  
         
        The experimental design is specified as:  
          cfg.ivar  = independent variable, row number of the design that contains the labels of the conditions to be compared (default=1)  
          cfg.uvar  = optional, row number of design that contains the labels of the units-of-observation, i.e. subjects or trials (default=2)  
         
        The labels for the independent variable should be specified as the number 1 and 2.  
        The labels for the unit of observation should be integers ranging from 1 to the  
        total number of observations (subjects or trials).  
         
        The cfg.uvar option is only needed for paired data, you should leave it empty  
        for non-paired data.  
         
        See https://www.statisticshowto.datasciencecentral.com/bayes-factor-definition/ for some background.  
         
        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/statfun/ft_statfun_bayesfactor.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statfun_bayesfactor", *args, **kwargs)
