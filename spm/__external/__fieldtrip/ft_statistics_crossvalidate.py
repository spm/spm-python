from spm._runtime import Runtime


def ft_statistics_crossvalidate(*args, **kwargs):
    r"""
      FT_STATISTICS_CROSSVALIDATE performs cross-validation using a prespecified  
        multivariate analysis. It is not recommended to call this function directly,  
        but instead you should call the function that is associated with the type of data on   
        which you want to perform the test. This is because important data bookkeeping   
        operations on the data are performed in the higher-level functions, which are  
        assumed to have been handled correctly for the input arguments into this function.   
        Also, notably, a prespecified randomseed in the cfg is handled in the higher  
        level function, not here.  
         
        Use as  
          stat = ft_timelockstatistics(cfg, data1, data2, data3, ...)  
          stat = ft_freqstatistics    (cfg, data1, data2, data3, ...)  
          stat = ft_sourcestatistics  (cfg, data1, data2, data3, ...)  
         
        where the data is obtained from FT_TIMELOCKANALYSIS, FT_FREQANALYSIS or  
        FT_SOURCEANALYSIS respectively, or from FT_TIMELOCKGRANDAVERAGE,  
        FT_FREQGRANDAVERAGE or FT_SOURCEGRANDAVERAGE respectively   
        and with cfg.method = 'crossvalidate'  
         
        The configuration options that can be specified are:  
          cfg.mva           = a multivariate analysis (default = {dml.standardizer dml.svm})  
          cfg.statistic     = a cell-array of statistics to report (default = {'accuracy' 'binomial'})  
          cfg.nfolds        = number of cross-validation folds (default = 5)  
          cfg.resample      = true/false; upsample less occurring classes during  
                              training and downsample often occurring classes  
                              during testing (default = false)  
         
        This returns:  
          stat.statistic = the statistics to report  
          stat.model     = the models associated with this multivariate analysis  
         
        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS, FT_SOURCESTATISTICS  
        FT_STATISTICS_ANALYTIC, FT_STATISTICS_MONTECARLO, FT_STATISTICS_MVPA,  
        FT_STATISTICS_CROSSVALIDATE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_statistics_crossvalidate.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_statistics_crossvalidate", *args, **kwargs)
