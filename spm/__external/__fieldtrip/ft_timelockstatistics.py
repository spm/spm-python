from spm.__wrapper__ import Runtime


def ft_timelockstatistics(*args, **kwargs):
    """
      FT_TIMELOCKSTATISTICS  computes significance probabilities and/or critical values of a parametric statistical test  
        or a non-parametric permutation test.  
         
        Use as  
          [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)  
        where the input data is the result from either FT_TIMELOCKANALYSIS or  
        FT_TIMELOCKGRANDAVERAGE.  
         
        The configuration can contain the following options for data selection  
          cfg.channel     = Nx1 cell-array with selection of channels (default = 'all'),  
                            see FT_CHANNELSELECTION for details  
          cfg.latency     = [begin end] in seconds or 'all' (default = 'all')  
          cfg.avgoverchan = 'yes' or 'no'                   (default = 'no')  
          cfg.avgovertime = 'yes' or 'no'                   (default = 'no')  
          cfg.parameter   = string                          (default = 'trial' or 'avg')  
         
        Furthermore, the configuration should contain  
          cfg.method       = different methods for calculating the significance probability and/or critical value  
                           'montecarlo'    get Monte-Carlo estimates of the significance probabilities and/or critical values from the permutation distribution,  
                           'analytic'      get significance probabilities and/or critical values from the analytic reference distribution (typically, the sampling distribution under the null hypothesis),  
                           'stats'         use a parametric test from the MATLAB statistics toolbox,  
                           'mvpa'          use functionality from the MVPA-light toolbox for classification or multivariate regression  
         
        The other cfg options depend on the method that you select. You  
        should read the help of the respective subfunction FT_STATISTICS_XXX  
        for the corresponding configuration options and for a detailed  
        explanation of each method.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_TIMELOCKANALYSIS, FT_TIMELOCKGRANDAVERAGE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_timelockstatistics.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_timelockstatistics", *args, **kwargs)
