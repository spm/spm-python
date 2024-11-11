from spm.__wrapper__ import Runtime


def ft_appendtimelock(*args, **kwargs):
    """
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
         
        See also FT_TIMELOCKANALYSIS, FT_DATATYPE_TIMELOCK, FT_APPENDDATA, FT_APPENDFREQ,  
        FT_APPENDSOURCE, FT_APPENDSENS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_appendtimelock.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_appendtimelock", *args, **kwargs)
