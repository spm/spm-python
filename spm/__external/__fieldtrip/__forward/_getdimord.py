from spm._runtime import Runtime


def _getdimord(*args, **kwargs):
    r"""
      GETDIMORD determine the dimensions and order of a data field in a FieldTrip  
        structure.  
         
        Use as  
          dimord = getdimord(data, field)  
         
        See also GETDIMSIZ, GETDATFIELD, FIXDIMORD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/getdimord.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getdimord", *args, **kwargs)
