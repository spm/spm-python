from spm.__wrapper__ import Runtime


def ft_statfun_indepsamplesT(*args, **kwargs):
    """
      FT_STATFUN_INDEPSAMPLEST calculates the independent samples T-statistic on the  
        biological data in dat (the dependent variable), using the information on the  
        independent variable (ivar) in design.  
         
        Use this function by calling one of the high-level statistics functions as  
          [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)  
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)  
          [stat] = ft_sourcestatistics(cfg, source1, source2, ...)  
        with the following configuration option:  
          cfg.statistic = 'ft_statfun_indepsamplesT'  
         
        You can specify the following configuration options:  
          cfg.computestat    = 'yes' or 'no', calculate the statistic (default='yes')  
          cfg.computecritval = 'yes' or 'no', calculate the critical values of the test statistics (default='no')  
          cfg.computeprob    = 'yes' or 'no', calculate the p-values (default='no')  
         
        The following options are relevant if cfg.computecritval='yes' and/or cfg.computeprob='yes':  
          cfg.alpha = critical alpha-level of the statistical test (default=0.05)  
          cfg.tail  = -1, 0, or 1, left, two-sided, or right (default=1)  
                      cfg.tail in combination with cfg.computecritval='yes'  
                      determines whether the critical value is computed at  
                      quantile cfg.alpha (with cfg.tail=-1), at quantiles  
                      cfg.alpha/2 and (1-cfg.alpha/2) (with cfg.tail=0), or at  
                      quantile (1-cfg.alpha) (with cfg.tail=1).  
         
        The experimental design is specified as:  
          cfg.ivar  = independent variable, row number of the design that contains the labels of the conditions to be compared (default=1)  
         
        The labels for the independent variable should be specified as the number 1 and 2.  
         
        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/statfun/ft_statfun_indepsamplesT.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statfun_indepsamplesT", *args, **kwargs)
