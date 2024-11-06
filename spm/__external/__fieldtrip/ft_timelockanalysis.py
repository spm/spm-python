from spm.__wrapper__ import Runtime


def ft_timelockanalysis(*args, **kwargs):
    """
      FT_TIMELOCKANALYSIS computes the timelocked average ERP/ERF and optionally computes  
        the covariance matrix over the specified time window.  
         
        Use as  
          [timelock] = ft_timelockanalysis(cfg, data)  
         
        The data should be organised in a structure as obtained from FT_PREPROCESSING.   
        The configuration should be according to  
          cfg.channel            = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details  
          cfg.latency            = [begin end] in seconds, or 'all', 'minperiod', 'maxperiod', 'prestim', 'poststim' (default = 'all')  
          cfg.trials             = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.keeptrials         = 'yes' or 'no', return individual trials or average (default = 'no')  
          cfg.nanmean            = string, can be 'yes' or 'no' (default = 'yes')  
          cfg.normalizevar       = 'N' or 'N-1' (default = 'N-1')  
          cfg.covariance         = 'no' or 'yes' (default = 'no')  
          cfg.covariancewindow   = [begin end] in seconds, or 'all', 'minperiod', 'maxperiod', 'prestim', 'poststim' (default = 'all')  
          cfg.removemean         = 'yes' or 'no', for the covariance computation (default = 'yes')  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_TIMELOCKGRANDAVERAGE, FT_TIMELOCKSTATISTICS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_timelockanalysis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_timelockanalysis", *args, **kwargs)
