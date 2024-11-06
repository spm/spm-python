from spm.__wrapper__ import Runtime


def ft_appendfreq(*args, **kwargs):
    """
      FT_APPENDFREQ concatenates multiple frequency or time-frequency data structures  
        that have been processed separately. If the input data structures contain different  
        channels, it will be concatenated along the channel direction. If the channels are  
        identical in the input data structures, the data will be concatenated along the  
        repetition dimension.  
         
        Use as  
         combined = ft_appendfreq(cfg, freq1, freq2, ...)  
         
        The configuration should contain  
          cfg.parameter  = string, the name of the field to concatenate  
         
        The configuration can optionally contain  
          cfg.appenddim  = string, the dimension to concatenate over (default is automatic)  
          cfg.tolerance  = scalar, tolerance to determine how different the frequency and/or  
                           time axes are allowed to still be considered compatible (default = 1e-5)  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a  
        *.mat file on disk and/or the output data will be written to a *.mat file.  
        These mat files should contain only a single variable, corresponding with  
        the input/output structure.  
         
        See also FT_FREQANALYSIS, FT_DATATYPE_FREQ, FT_APPENDDATA, FT_APPENDTIMELOCK,  
        FT_APPENDSENS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_appendfreq.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_appendfreq", *args, **kwargs)
