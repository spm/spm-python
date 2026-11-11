from spm._runtime import Runtime


def _makessense(*args, **kwargs):
    r"""
      MAKESSENSE determines whether a some specific fields in a FieldTrip data structure  
        make sense.  
         
        Use as  
          status = makessense(data, field)  
         
        See also GETDIMORD, GETDIMSIZ, GETDATFIELD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/makessense.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("makessense", *args, **kwargs)
