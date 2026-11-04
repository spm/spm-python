from spm._runtime import Runtime


def _blc(*args, **kwargs):
    r"""
      BLC does a baseline correction using the prestimulus interval of the data  
         
          [data] = baseline(data, interval);  
          [data] = baseline(data, begin, end);  
         
        If no begin and end are specified, the whole timeinterval is  
        used for baseline correction.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/blc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("blc", *args, **kwargs)
