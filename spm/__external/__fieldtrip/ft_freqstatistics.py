from spm.__wrapper__ import Runtime


def ft_freqstatistics(*args, **kwargs):
    """
      FT_FREQSTATISTICS computes significance probabilities and/or critical  
        values of a parametric statistical test or a non-parametric permutation  
        test.  
         
        Use as  
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)  
        where the input data is the result from FT_FREQANALYSIS, FT_FREQDESCRIPTIVES  
        or from FT_FREQGRANDAVERAGE.  
         
        The configuration can contain the following options for data selection  
          cfg.channel     = Nx1 cell-array with selection of channels (default = 'all'),  
                            see FT_CHANNELSELECTION for details  
          cfg.latency     = [begin end] in seconds or 'all' (default = 'all')  
          cfg.frequency   = [begin end], can be 'all'       (default = 'all')  
          cfg.avgoverchan = 'yes' or 'no'                   (default = 'no')  
          cfg.avgovertime = 'yes' or 'no'                   (default = 'no')  
          cfg.avgoverfreq = 'yes' or 'no'                   (default = 'no')  
          cfg.parameter   = string                          (default = 'powspctrm')  
         
        If you specify cfg.correctm='cluster', then the following is required  
          cfg.neighbours  = neighbourhood structure, see FT_PREPARE_NEIGHBOURS  
         
        Furthermore, the configuration should contain  
          cfg.method       = different methods for calculating the significance probability and/or critical value  
                           'montecarlo'    get Monte-Carlo estimates of the significance probabilities and/or critical values from the permutation distribution,  
                           'analytic'      get significance probabilities and/or critical values from the analytic reference distribution (typically, the sampling distribution under the null hypothesis),  
                           'stats'         use a parametric test from the MATLAB statistics toolbox,  
                           'crossvalidate' use crossvalidation to compute predictive performance  
         
          cfg.design       = Nxnumobservations: design matrix (for examples/advice, please see the Fieldtrip wiki,  
                             especially cluster-permutation tutorial and the 'walkthrough' design-matrix section)  
         
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
         
        See also FT_FREQANALYSIS, FT_FREQDESCRIPTIVES, FT_FREQGRANDAVERAGE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_freqstatistics.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_freqstatistics", *args, **kwargs)
