from spm.__wrapper__ import Runtime


def ft_statfun_depsamplesFunivariate(*args, **kwargs):
    """
      FT_STATFUN_DEPSAMPLESFUNIIVARIATE calculates the univariate repeated-mesures ANOVA  
        on the biological data (the dependent variable), using the information on the  
        independent variable (ivar) in design.  
         
        Use this function by calling one of the high-level statistics functions as  
          [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)  
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)  
          [stat] = ft_sourcestatistics(cfg, source1, source2, ...)  
        with the following configuration option:  
          cfg.statistic = 'ft_statfun_depsamplesFunivariate'  
         
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
                      quantile (1-cfg.alpha) (with cfg.tail=1). For the  
                      Fstatistic only cfg.tail = 1 makes sense.  
         
        The experimental design is specified as:  
          cfg.ivar  = independent variable, row number of the design that contains the labels of the conditions to be compared (default=1)  
          cfg.uvar  = unit variable, row number of design that contains the labels of the units-of-observation, i.e. subjects or trials (default=2)  
         
        The labels for the independent variable should be specified as numbers ranging  
        from 1 to the number of conditions. The labels for the unit of observation should  
        be integers ranging from 1 to the total number of observations (subjects or trials).  
         
        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/statfun/ft_statfun_depsamplesFunivariate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statfun_depsamplesFunivariate", *args, **kwargs)
