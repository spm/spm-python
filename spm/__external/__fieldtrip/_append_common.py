from spm._runtime import Runtime


def _append_common(*args, **kwargs):
    r"""
      APPEND_COMMON is used for concatenating raw, timelock or freq data  
         
        The general bookkeeping and the correct specification of the cfg  
        should be taken care of by the calling function.  
         
        See FT_APPENDDATA, FT_APPENDTIMELOCK, FT_APPENDFREQ  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/append_common.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("append_common", *args, **kwargs)
