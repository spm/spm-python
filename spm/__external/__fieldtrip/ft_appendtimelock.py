from spm._runtime import Runtime


def ft_appendtimelock(*args, **kwargs):
    r"""
      FT_APPENDTIMELOCK concatenates multiple timelock (ERP/ERF) data structures that  
        have been processed separately. If the input data structures contain different  
        channels, it will be concatenated along the channel direction. If the channels are  
        identical in the input data structures, the data will be concatenated along the  
        repetition dimension.  
         
        Use as  
          combined = ft_appendtimelock(cfg, timelock1, timelock2, ...)  
         
        The configuration can contain  
          cfg.appenddim       = string, the dimension to concatenate over which to append,  
                                this can be 'chan' and 'rpt' (default is automatic)  
          cfg.tolerance       = scalar, tolerance to determine how different the time axes  
                                are allowed to still be considered compatible (default = 1e-5)  
          cfg.keepsampleinfo  = 'yes', 'no', 'ifmakessense' (default = 'ifmakessense')  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a  
        *.mat file on disk and/or the output data will be written to a *.mat file.  
        These mat files should contain only a single variable, corresponding with  
        the input/output structure.  
         
        If you encounter difficulties with memory usage, you can use  
          cfg.memory = 'low' or 'high', whether to be memory or computationally efficient, respectively (default = 'high')  
         
        See also FT_TIMELOCKANALYSIS, FT_DATATYPE_TIMELOCK, FT_APPENDDATA, FT_APPENDFREQ,  
        FT_APPENDSOURCE, FT_APPENDSENS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_appendtimelock.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_appendtimelock", *args, **kwargs)
