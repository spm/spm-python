from spm._runtime import Runtime


def ft_statistics_stats(*args, **kwargs):
    r"""
      FT_STATISTICS_STATS performs a massive univariate statistical test using the MATLAB  
        statistics toolbox. It is not recommended to call this function directly,  
        but instead you should call the function that is associated with the type of data on   
        which you want to perform the test. This is because important data bookkeeping   
        operations on the data are performed in the higher-level functions, which are  
        assumed to have been handled correctly for the input arguments into this function.   
         
        Use as  
          stat = ft_timelockstatistics(cfg, data1, data2, data3, ...)  
          stat = ft_freqstatistics    (cfg, data1, data2, data3, ...)  
          stat = ft_sourcestatistics  (cfg, data1, data2, data3, ...)  
         
        where the data is obtained from FT_TIMELOCKANALYSIS, FT_FREQANALYSIS or  
        FT_SOURCEANALYSIS respectively, or from FT_TIMELOCKGRANDAVERAGE,  
        FT_FREQGRANDAVERAGE or FT_SOURCEGRANDAVERAGE respectively   
        and with cfg.method = 'stats'  
         
        The configuration options that can be specified are:  
          cfg.alpha     = number, critical value for rejecting the null-hypothesis (default = 0.05)  
          cfg.tail      = number, -1, 1 or 0 (default = 0)  
          cfg.feedback  = string, 'gui', 'text', 'textbar' or 'no' (default = 'textbar')  
          cfg.method    = 'stats'  
          cfg.statistic = 'ttest'          test against a mean of zero  
                          'ttest2'         compare the mean in two conditions  
                          'paired-ttest'  
                          'anova1'  
                          'kruskalwallis'  
                          'signtest'  
                          'signrank'  
                          'pearson'  
                          'kendall'  
                          'spearman'  
         
        See also TTEST, TTEST2, KRUSKALWALLIS, SIGNTEST, SIGNRANK, FT_TIMELOCKSTATISTICS,  
        FT_FREQSTATISTICS, FT_SOURCESTATISTICS FT_STATISTICS_ANALYTIC, FT_STATISTICS_STATS,  
        FT_STATISTICS_MONTECARLO, FT_STATISTICS_CROSSVALIDATE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_statistics_stats.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_statistics_stats", *args, **kwargs)
