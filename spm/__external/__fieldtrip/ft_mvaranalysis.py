from spm.__wrapper__ import Runtime


def ft_mvaranalysis(*args, **kwargs):
    """
      FT_MVARANALYSIS performs multivariate autoregressive modeling on  
        time series data over multiple trials.  
         
        Use as  
          [mvardata] = ft_mvaranalysis(cfg, data)  
         
        The input data should be organised in a structure as obtained from  
        the FT_PREPROCESSING function. The configuration depends on the type  
        of computation that you want to perform.  
        The output is a data structure of datatype 'mvar' which contains the  
        multivariate autoregressive coefficients in the field coeffs, and the  
        covariance of the residuals in the field noisecov.  
         
        The configuration should contain:  
          cfg.method     = the name of the toolbox containing the function for the  
                            actual computation of the ar-coefficients  
                            this can be 'biosig' (default) or 'bsmart'  
                            you should have a copy of the specified toolbox in order  
                            to use mvaranalysis (both can be downloaded directly).  
          cfg.mvarmethod = scalar (only required when cfg.method = 'biosig').  
                            default is 2, relates to the algorithm used for the  
                            computation of the AR-coefficients by mvar.m  
          cfg.order      = scalar, order of the autoregressive model (default=10)  
          cfg.channel    = 'all' (default) or list of channels for which an mvar model  
                            is fitted. (Do NOT specify if cfg.channelcmb is  
                            defined)  
          cfg.channelcmb = specify channel combinations as a  
                            two-column cell-array with channels in each column between  
                            which a bivariate model will be fit (overrides  
                            cfg.channel)  
          cfg.keeptrials = 'no' (default) or 'yes' specifies whether the coefficients  
                            are estimated for each trial separately, or on the  
                            concatenated data  
          cfg.jackknife  = 'no' (default) or 'yes' specifies whether the coefficients  
                            are estimated for all leave-one-out sets of trials  
          cfg.zscore     = 'no' (default) or 'yes' specifies whether the channel data  
                             are z-transformed prior to the model fit. This may be  
                             necessary if the magnitude of the signals is very different  
                             e.g. when fitting a model to combined MEG/EMG data  
          cfg.demean     = 'yes' (default) or 'no' explicit removal of DC-offset  
          cfg.ems        = 'no' (default) or 'yes' explicit removal ensemble mean  
         
        ft_mvaranalysis can be used to obtain one set of coefficients across  
        all time points in the data, also when the trials are of varying length.  
         
        ft_mvaranalysis can be also used to obtain time-dependent sets of  
        coefficients based on a sliding window. In this case the input cfg  
        should contain:  
         
          cfg.t_ftimwin = the width of the sliding window on which the coefficients  
                           are estimated  
          cfg.toi       = [t1 t2 ... tx] the time points at which the windows are  
                           centered  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_PREPROCESSING, FT_SOURCESTATISTICS, FT_FREQSTATISTICS,  
        FT_TIMELOCKSTATISTICS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_mvaranalysis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_mvaranalysis", *args, **kwargs)
