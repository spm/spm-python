from spm.__wrapper__ import Runtime


def ft_statistics_crossvalidate(*args, **kwargs):
    """
      FT_STATISTICS_CROSSVALIDATE performs cross-validation using a prespecified  
        multivariate analysis. This function should not be called directly, instead you  
        should call the function that is associated with the type of data on which you want  
        to perform the test.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_statistics_crossvalidate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statistics_crossvalidate", *args, **kwargs)
