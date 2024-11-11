from spm.__wrapper__ import Runtime


def ft_statfun_cohensd(*args, **kwargs):
    """
      FT_STATFUN_COHENSD computes the effect size according to Cohen's d. This function  
        supports both unpaired and paired designs.  
         
        The table below contains descriptors for magnitudes of Cohen's d.  
          Very small  0.01  
          Small       0.20  
          Medium      0.50  
          Large       0.80  
          Very large  1.20  
          Huge        2.00  
         
        Use this function by calling one of the high-level statistics functions as  
          [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)  
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)  
          [stat] = ft_sourcestatistics(cfg, source1, source2, ...)  
        with the following configuration option:  
          cfg.statistic = 'ft_statfun_cohensd'  
         
        The experimental design is specified as:  
          cfg.ivar  = independent variable, row number of the design that contains the labels of the conditions to be compared (default=1)  
          cfg.uvar  = optional, row number of design that contains the labels of the units-of-observation, i.e. subjects or trials (default=2)  
         
        The labels for the independent variable should be specified as the number 1 and 2.  
        The labels for the unit of observation should be integers ranging from 1 to the  
        total number of observations (subjects or trials).  
         
        The cfg.uvar option is only needed for paired data, you should leave it empty  
        for non-paired data.  
         
        See https://en.wikipedia.org/wiki/Effect_size#Cohen.27s_d for a description  
        and https://www.psychometrica.de/effect_size.html for an online computation tool.  
         
        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/statfun/ft_statfun_cohensd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statfun_cohensd", *args, **kwargs)
