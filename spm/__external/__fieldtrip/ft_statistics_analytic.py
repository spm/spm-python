from spm.__wrapper__ import Runtime


def ft_statistics_analytic(*args, **kwargs):
    """
      FT_STATISTICS_ANALYTIC performs a parametric statistical test on the data, based on  
        a known (i.e. analytic) distribution of the test statistic. This function should  
        not be called directly, instead you should call the function that is associated  
        with the type of data on which you want to perform the test.  
         
        Use as  
          stat = ft_timelockstatistics(cfg, data1, data2, data3, ...)  
          stat = ft_freqstatistics    (cfg, data1, data2, data3, ...)  
          stat = ft_sourcestatistics  (cfg, data1, data2, data3, ...)  
         
        where the data is obtained from FT_TIMELOCKANALYSIS, FT_FREQANALYSIS or  
        FT_SOURCEANALYSIS respectively, or from FT_TIMELOCKGRANDAVERAGE,  
        FT_FREQGRANDAVERAGE or FT_SOURCEGRANDAVERAGE respectively   
        and with cfg.method = 'analytic'  
         
        The configuration options that can be specified are:  
          cfg.statistic        = string, statistic to compute for each sample or voxel (see below)  
          cfg.correctm         = string, apply multiple-comparison correction, 'no', 'bonferroni', 'holm', 'hochberg', 'fdr' (default = 'no')  
          cfg.alpha            = number, critical value for rejecting the null-hypothesis (default = 0.05)  
          cfg.tail             = number, -1, 1 or 0 (default = 0)  
          cfg.ivar             = number or list with indices, independent variable(s)  
          cfg.uvar             = number or list with indices, unit variable(s)  
          cfg.wvar             = number or list with indices, within-block variable(s)  
         
        The parametric statistic that is computed for each sample (and for  
        which the analytic probability of the null-hypothesis is computed) is  
        specified as  
          cfg.statistic       = 'indepsamplesT'           independent samples T-statistic,  
                                'indepsamplesF'           independent samples F-statistic,  
                                'indepsamplesregrT'       independent samples regression coefficient T-statistic,  
                                'indepsamplesZcoh'        independent samples Z-statistic for coherence,  
                                'depsamplesT'             dependent samples T-statistic,  
                                'depsamplesFmultivariate' dependent samples F-statistic MANOVA,  
                                'depsamplesregrT'         dependent samples regression coefficient T-statistic,  
                                'actvsblT'                activation versus baseline T-statistic.  
        or you can specify your own low-level statistical function.  
         
        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS, FT_SOURCESTATISTICS  
        FT_STATISTICS_MONTECARLO, FT_STATISTICS_STATS, FT_STATISTICS_MVPA,  
        FT_STATISTICS_CROSSVALIDATE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_statistics_analytic.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statistics_analytic", *args, **kwargs)
