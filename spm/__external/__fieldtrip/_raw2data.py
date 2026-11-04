from spm._runtime import Runtime


def _raw2data(*args, **kwargs):
    r"""
      RAW2DATA is a helper function that converts raw data to various types of  
        averages. This function is used to apply the analysis steps that were  
        written for use on preprocessed data also on averaged data.  
         
        This function is the counterpart of DATA2RAW and is used in MEGREALIGN, MEGPLANAR, MEGREPAIR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/raw2data.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("raw2data", *args, **kwargs)
