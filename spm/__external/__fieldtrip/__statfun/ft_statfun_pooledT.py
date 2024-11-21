from spm.__wrapper__ import Runtime


def ft_statfun_pooledT(*args, **kwargs):
    """
      FT_STATFUN_POOLEDT computes the pooled t-value over a number of replications. The  
        idea behind this function is that you first (prior to calling this function)  
        compute a contrast between two conditions per subject, and that subsequently you  
        test this over subjects using random sign-flipping.  
         
        Use this function by calling one of the high-level statistics functions as  
          [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)  
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)  
          [stat] = ft_sourcestatistics(cfg, source1, source2, ...)  
        with the following configuration option  
          cfg.statistic = 'ft_statfun_pooledT'  
         
        The expected values for the pooled-t, which is zero according to H0, have to be  
        passed as pseudo-values. The subject-specific t-values will be randomly swapped with  
        the pseudo-values and the difference is computed; in effect this implements random  
        sign-flipping.  
         
        The randimization distribution (with optional clustering) of the randomly  
        sign-flipped pooled-t values is computed and used for statistical inference.  
         
        Note that, although the output of this function is to be interpreted as a  
        fixed-effects statistic, the statistical inference based on the comparison of the  
        observed pooled t-values with the randomization distribution is not a fixed-effect  
        statistic, one or a few outlier will cause the randomization distribution to  
        broaden and result in the conclusion of "not significant".  
         
        The experimental design is specified as:  
          cfg.ivar  = independent variable, row number of the design that contains the labels of the conditions to be sign-flipped (default=1)  
         
        The labels independent variable should be specified as the number 1 for the  
        observed t-values and 2 for the pseudo-values.  
         
        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/statfun/ft_statfun_pooledT.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statfun_pooledT", *args, **kwargs)
