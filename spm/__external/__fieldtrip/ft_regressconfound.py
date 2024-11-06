from spm.__wrapper__ import Runtime


def ft_regressconfound(*args, **kwargs):
    """
      FT_REGRESSCONFOUND estimates the regression weight of a set of confounds  
        using a General Linear Model (GLM) and removes the estimated contribution  
        from the single-trial data.  
         
        Use as  
          timelock = ft_regressconfound(cfg, timelock)  
        or as  
          freq     = ft_regressconfound(cfg, freq)  
        or as  
          source   = ft_regressconfound(cfg, source)  
         
        where timelock, freq, or, source come from FT_TIMELOCKANALYSIS,  
        FT_FREQANALYSIS, or FT_SOURCEANALYSIS respectively, with keeptrials = 'yes'  
         
        The cfg argument is a structure that should contain  
          cfg.confound    = matrix, [Ntrials X Nconfounds], may not contain NaNs  
         
        The following configuration options are supported:  
          cfg.reject      = vector, [1 X Nconfounds], listing the confounds that  
                            are to be rejected (default = 'all')  
          cfg.normalize   = string, 'yes' or 'no', normalizing confounds (default = 'yes')  
          cfg.output      = 'residual' (default), 'beta', or 'model'.  
                            If 'residual' is specified, the output is a data  
                            structure containing the residuals after regressing  
                            out the in cfg.reject listed confounds. If 'beta' or 'model'  
                            is specified, the output is a data structure containing  
                            the regression weights or the model, respectively.  
         
        This method is described by Stolk et al., Online and offline tools for head  
        movement compensation in MEG (Neuroimage, 2013)  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_REJECTCOMPONENT, FT_REJECTARTIFACT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_regressconfound.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_regressconfound", *args, **kwargs)
