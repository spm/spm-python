from spm.__wrapper__ import Runtime


def ft_denoise_tsr(*args, **kwargs):
    """
      FT_DENOISE_TSR performs a regression analysis, using a (time-shifted set  
        of) reference signal(s) as independent variable. It is a generic  
        implementation of the method described by De Cheveigne  
        (https://doi.org/10.1016/j.jneumeth.2007.06.003), or can be  
        used to compute temporal-response-functions (see e.g. Crosse  
        (https://doi.org/10.3389/fnhum.2016.00604)), or  
        spatial filters based on canonical correlation (see Thielen  
        (https://doi.org/10.1371/journal.pone.0133797))  
         
        Use as  
          [dataout] = ft_denoise_tsr(cfg, data)  
          [dataout] = ft_denoise_tsr(cfg, data, refdata)  
        where "data" is a raw data structure that was obtained with FT_PREPROCESSING. If  
        you specify the additional input "refdata", the specified reference channels for  
        the regression will be taken from this second data structure. This can be useful  
        when reference-channel specific preprocessing needs to be done (e.g. low-pass  
        filtering).  
         
        The output structure dataout contains the denoised data in a format consistent  
        with the output of FT_PREPROCESSING.  
         
        The configuration options are:  
          cfg.refchannel         = the channels used as reference signal (default = 'MEGREF'), see FT_SELECTDATA  
          cfg.channel            = the channels to be denoised (default = 'all'), see FT_SELECTDATA  
          cfg.method             = string, 'mlr', 'cca', 'pls', 'svd', option specifying the criterion for the regression  
                                   (default = 'mlr')  
          cfg.reflags            = integer array, specifying temporal lags (in msec) by which to shift refchannel  
                                   with respect to data channels  
          cfg.trials             = integer array, trials to be used in regression, see FT_SELECTDATA  
          cfg.testtrials         = cell-array or string, trial indices to be used as test folds in a cross-validation scheme  
                                   (numel(cfg.testrials == number of folds))  
          cfg.nfold              = scalar, indicating the number of test folds to  
                                   use in a cross-validation scheme  
          cfg.standardiserefdata = string, 'yes' or 'no', whether or not to standardise reference data  
                                   prior to the regression (default = 'no')  
          cfg.standardisedata    = string, 'yes' or 'no', whether or not to standardise dependent variable  
                                   prior to the regression (default = 'no')  
          cfg.demeanrefdata      = string, 'yes' or 'no', whether or not to make  
                                   reference data zero mean prior to the regression (default = 'no')  
          cfg.demeandata         = string, 'yes' or 'no', whether or not to make  
                                   dependent variable zero mean prior to the regression (default = 'no')  
          cfg.threshold          = integer array, ([1 by 2] or [1 by numel(cfg.channel) + numel(cfg.reflags)]),  
                                   regularization or shrinkage ('lambda') parameter to be loaded on the diagonal of the  
                                   penalty term (if cfg.method == 'mlrridge' or 'mlrqridge')  
          cfg.updatesens         = string, 'yes' or 'no' (default = 'yes')  
          cfg.perchannel         = string, 'yes' or 'no', or logical, whether or not to perform estimation of beta weights  
                                   separately per channel  
          cfg.output             = string, 'model' or 'residual' (defaul = 'model'),  
                                   specifies what is outputed in .trial field in <dataout>  
          cfg.performance        = string, 'pearson' or 'r-squared' (default =  
                                   'pearson'), indicating what performance metric is outputed in .weights(k).performance  
                                   field of <dataout> for the k-th fold  
          cfg.covmethod          = string, 'finite', or 'overlapfinite' (default  
                                   = 'finite'), compute covariance for the auto  
                                   terms on the finite datapoints per channel, or  
                                   only on the datapoints that are finite for the  
                                   cross terms. If there is a large number of  
                                   unshared nans across datasets, and if this number  
                                   is large in comparison to the total number of  
                                   datapoints the 'finite' method may become unstable.  
         
        If cfg.threshold is 1 x 2 integer array, the cfg.threshold(1) parameter scales  
        uniformly in the dimension of predictor variable and cfg.threshold(2) in the  
        space of response variable.  
         
        See also FT_PREPROCESSING, FT_DENOISE_SYNTHETIC, FT_DENOISE_PCA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_denoise_tsr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_denoise_tsr", *args, **kwargs)
