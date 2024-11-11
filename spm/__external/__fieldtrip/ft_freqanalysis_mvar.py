from spm.__wrapper__ import Runtime


def ft_freqanalysis_mvar(*args, **kwargs):
    """
      FT_FREQANALYSIS_MVAR performs frequency analysis on  
        mvar data, by fourier transformation of the coefficients. The output  
        contains cross-spectral density, spectral transfer matrix, and the  
        covariance of the innovation noise. The dimord = 'chan_chan(_freq)(_time)  
         
        The function is stand-alone, but is typically called through  
        FT_FREQANALYSIS, specifying cfg.method = 'mvar'.  
         
        Use as  
          [freq] = ft_freqanalysis(cfg, data), with cfg.method = 'mvar'  
         
        or  
         
          [freq] = ft_freqanalysis_mvar(cfg, data)  
         
        The input data structure should be a data structure created by  
        FT_MVARANALYSIS, i.e. a data-structure of type 'mvar'.  
         
        The configuration can contain:  
          cfg.foi = vector with the frequencies at which the spectral quantities  
                      are estimated (in Hz). Default: 0:1:Nyquist  
          cfg.feedback = 'none', or any of the methods supported by FT_PROGRESS,  
                           for providing feedback to the user in the command  
                           window.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_MVARANALYSIS, FT_DATATYPE_MVAR, FT_PROGRESS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_freqanalysis_mvar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_freqanalysis_mvar", *args, **kwargs)
