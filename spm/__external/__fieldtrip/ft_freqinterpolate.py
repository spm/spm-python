from spm.__wrapper__ import Runtime


def ft_freqinterpolate(*args, **kwargs):
    """
      FT_FREQINTERPOLATE interpolates frequencies by looking at neighbouring  
        values or simply replaces a piece in the spectrum by NaN.  
         
        Use as  
          freq = ft_freqinterpolate(cfg, freq)  
        where freq is the output of FT_FREQANALYSIS or FT_FREQDESCRIPTIVES and the  
        configuration may contain  
          cfg.method   = 'nan', 'linear' (default = 'nan')  
          cfg.foilim   = Nx2 matrix with begin and end of each interval to be  
                         interpolated (default = [49 51; 99 101; 149 151])  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_FREQANALYSIS, FT_FREQDESCRIPTIVES, FT_FREQSIMULATION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_freqinterpolate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_freqinterpolate", *args, **kwargs)
