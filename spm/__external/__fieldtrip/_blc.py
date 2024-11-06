from spm.__wrapper__ import Runtime


def _blc(*args, **kwargs):
    """
      BLC does a baseline correction using the prestimulus interval of the data  
         
          [data] = baseline(data, interval);  
          [data] = baseline(data, begin, end);  
         
        If no begin and end are specified, the whole timeinterval is  
        used for baseline correction.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/blc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("blc", *args, **kwargs)
