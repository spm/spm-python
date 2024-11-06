from spm.__wrapper__ import Runtime


def _append_common(*args, **kwargs):
    """
      APPEND_COMMON is used for concatenating raw, timelock or freq data  
         
        The general bookkeeping and the correct specification of the cfg  
        should be taken care of by the calling function.  
         
        See FT_APPENDDATA, FT_APPENDTIMELOCK, FT_APPENDFREQ  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/append_common.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("append_common", *args, **kwargs)
