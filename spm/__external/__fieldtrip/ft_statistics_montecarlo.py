from spm.__wrapper__ import Runtime


def ft_statistics_montecarlo(*args, **kwargs):
    """
      FT_STATISTICS_MONTECARLO performs a nonparametric statistical test by calculating  
        Monte-Carlo estimates of the significance probabilities and/or critical values from  
        the permutation distribution. This function should not be called directly, instead  
        you should call the function that is associated with the type of data on which you  
        want to perform the test.  
         
        Use as  
          stat = ft_timelockstatistics(cfg, data1, data2, data3, ...)  
          stat = ft_freqstatistics    (cfg, data1, data2, data3, ...)  
          stat = ft_sourcestatistics  (cfg, data1, data2, data3, ...)  
         
        where the data is obtained from FT_TIMELOCKANALYSIS, FT_FREQANALYSIS or  
        FT_SOURCEANALYSIS respectively, or from FT_TIMELOCKGRANDAVERAGE,  
        FT_FREQGRANDAVERAGE or FT_SOURCEGRANDAVERAGE respectively   
        and with cfg.method = 'montecarlo'  
         
        The configuration options that can be specified are:  
          cfg.numrandomization = number of randomizations, can be 'all'  
          cfg.correctm         = string, apply multiple-comparison correction, 'no', 'max', cluster', 'tfce', 'bonferroni', 'holm', 'hochberg', 'fdr' (default = 'no')  
          cfg.alpha            = number, critical value for rejecting the null-hypothesis per tail (default = 0.05)  
          cfg.tail             = number, -1, 1 or 0 (default = 0)  
          cfg.correcttail      = string, correct p-values or alpha-values when doing a two-sided test, 'alpha','prob' or 'no' (default = 'no')  
          cfg.ivar             = number or list with indices, independent variable(s)  
          cfg.uvar             = number or list with indices, unit variable(s)  
          cfg.wvar             = number or list with indices, within-cell variable(s)  
          cfg.cvar             = number or list with indices, control variable(s)  
          cfg.feedback         = string, 'gui', 'text', 'textbar' or 'no' (default = 'text')  
          cfg.randomseed       = string, 'yes', 'no' or a number (default = 'yes')  
         
        If you use a cluster-based statistic, you can specify the following options that  
        determine how the single-sample or single-voxel statistics will be thresholded and  
        combined into one statistical value per cluster.  
          cfg.clusterstatistic = how to combine the single samples that belong to a cluster, 'maxsum', 'maxsize', 'wcm' (default = 'maxsum')  
                                 the option 'wcm' refers to 'weighted cluster mass', a statistic that combines cluster size and intensity;   
                                 see Hayasaka & Nichols (2004) NeuroImage for details  
          cfg.clusterthreshold = method for single-sample threshold, 'parametric', 'nonparametric_individual', 'nonparametric_common' (default = 'parametric')  
          cfg.clusteralpha     = for either parametric or nonparametric thresholding per tail (default = 0.05)  
          cfg.clustercritval   = for parametric thresholding (default is determined by the statfun)  
          cfg.clustertail      = -1, 1 or 0 (default = 0)  
         
        To include the channel dimension for clustering of channel level data, you should specify  
          cfg.neighbours       = neighbourhood structure, see FT_PREPARE_NEIGHBOURS  
        If you specify an empty neighbourhood structure, clustering will only be done  
        over frequency and/or time and not over neighbouring channels.  
         
        The statistic that is computed for each sample in each random reshuffling  
        of the data is specified as  
          cfg.statistic       = 'indepsamplesT'           independent samples T-statistic,  
                                'indepsamplesF'           independent samples F-statistic,  
                                'indepsamplesregrT'       independent samples regression coefficient T-statistic,  
                                'indepsamplesZcoh'        independent samples Z-statistic for coherence,  
                                'depsamplesT'             dependent samples T-statistic,  
                                'depsamplesFmultivariate' dependent samples F-statistic MANOVA,  
                                'depsamplesregrT'         dependent samples regression coefficient T-statistic,  
                                'actvsblT'                activation versus baseline T-statistic.  
        or you can specify your own low-level statistical function.  
         
        You can also use a custom statistic of your choice that is sensitive to the  
        expected effect in the data. You can implement the statistic in a "statfun" that  
        will be called for each randomization. The requirements on a custom statistical  
        function is that the function is called ft_statfun_xxx, and that the function returns  
        a structure with a "stat" field containing the single sample statistical values.  
        Have a look at the functions in the fieldtrip/statfun directory (e.g.   
        FT_STATFUN_INDEPSAMPLEST) for the correct format of the input and output.  
         
        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS, FT_SOURCESTATISTICS,  
        FT_STATISTICS_ANALYTIC, FT_STATISTICS_STATS, FT_STATISTICS_MVPA,  
        FT_STATISTICS_CROSSVALIDATE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_statistics_montecarlo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statistics_montecarlo", *args, **kwargs)
