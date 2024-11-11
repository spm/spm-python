from spm.__wrapper__ import Runtime


def ft_eventtiminganalysis(*args, **kwargs):
    """
      FT_EVENTTIMINGANALYSIS computes a model of single trial event- related activity,  
        by estimating per trial the latency (and amplitude) of event-related signal  
        components.  
         
        Use as  
          [dataout] = ft_eventtiminganalysis(cfg, data)  
        where data is single-channel raw data as obtained by FT_PREPROCESSING  
        and cfg is a configuration structure according to  
         
          cfg.method  = method for estimating event-related activity  
                        'aseo', analysis of single-trial ERP and ongoing  
                                activity (according to Xu et al, 2009)  
                        'gbve', graph-based variability estimation  
                                (according to Gramfort et al, IEEE TBME 2009)  
          cfg.channel = Nx1 cell-array with selection of channels (default = 'all'),  
                        see FT_CHANNELSELECTION for details  
          cfg.trials  = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.output  = 'model', or 'residual', which returns the modelled data,  
                        or the residuals.  
         
        Method specific options are specified in the appropriate substructure.  
         
        For the ASEO method, the following options can be specified:  
          cfg.aseo.noiseEstimate   = 'non-parametric' or 'parametric', estimate noise  
                                     using parametric or non-parametric (default) method  
          cfg.aseo.tapsmofrq       = value, smoothing parameter of noise for  
                                     nonparametric estimation (default = 5)  
          cfg.aseo.jitter          = value, time jitter in initial timewindow  
                                     estimate (in seconds). default 0.050 seconds  
          cfg.aseo.numiteration    = value, number of iteration (default = 1)  
          cfg.aseo.initlatency     = Nx2 matrix, initial set of latencies in seconds of event-  
                                     related components, give as [comp1start, comp1end;  
                                     comp2start, comp2end] (default not  
                                     specified). For multiple channels it should  
                                     be a cell-array, one matrix per channel  
         Alternatively, rather than specifying a (set of latencies), one can also  
         specify:  
         
          cfg.aseo.initcomp        = vector, initial estimate of the waveform  
                                     components. For multiple channels it should  
                                     be a cell-array, one matrix per channel.  
         
        For the GBVE method, the following options can be specified:  
          cfg.gbve.sigma             = vector, range of sigma values to explore in  
                                       cross-validation loop (default: 0.01:0.01:0.2)  
          cfg.gbve.distance          = scalar, distance metric to use as  
                                       evaluation criterion, see plugin code for  
                                       more informatoin  
          cfg.gbve.alpha             = vector, range of alpha values to explor in  
                                       cross-validation loop (default: [0 0.001 0.01 0.1])  
          cfg.gbve.exponent          = scalar, see plugin code for information  
          cfg.gbve.use_maximum       = boolean, (default: 1) consider the positive going peak  
          cfg.gbve.show_pca          = boolean, see plugin code (default 0)  
          cfg.gbve.show_trial_number = boolean, see plugin code (default 0)  
          cfg.gbve.verbose           = boolean (default: 1)  
          cfg.gbve.disp_log          = boolean, see plugin code (default 0)  
          cfg.gbve.latency           = vector [min max], latency range in s  
                                       (default: [-inf inf])  
          cfg.gbve.xwin              = scalar smoothing parameter for moving  
                                       average smoothing (default: 1), see  
                                       eeglab's movav function for more  
                                       information.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_SINGLETRIALANALYSIS_ASEO  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_eventtiminganalysis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_eventtiminganalysis", *args, **kwargs)
