from spm.__wrapper__ import Runtime


def ft_freqgrandaverage(*args, **kwargs):
    """
      FT_FREQGRANDAVERAGE computes the average powerspectrum or time-frequency spectrum  
        over multiple subjects  
         
        Use as  
          [grandavg] = ft_freqgrandaverage(cfg, freq1, freq2, freq3...)  
         
        The input data freq1..N are obtained from either FT_FREQANALYSIS with  
        keeptrials=no or from FT_FREQDESCRIPTIVES. The configuration structure  
        can contain  
          cfg.keepindividual = 'yes' or 'no' (default = 'no')  
          cfg.foilim         = [fmin fmax] or 'all', to specify a subset of frequencies (default = 'all')  
          cfg.toilim         = [tmin tmax] or 'all', to specify a subset of latencies (default = 'all')  
          cfg.channel        = Nx1 cell-array with selection of channels (default = 'all'),  
                               see FT_CHANNELSELECTION for details  
          cfg.parameter      = string or cell-array of strings indicating which  
                               parameter(s) to average. default is set to  
                               'powspctrm', if it is present in the data.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure. For this particular function, the input should be  
        specified as a cell-array.  
         
        See also FT_TIMELOCKGRANDAVERAGE, FT_FREQANALYSIS, FT_FREQDESCRIPTIVES,  
        FT_FREQBASELINE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_freqgrandaverage.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_freqgrandaverage", *args, **kwargs)
