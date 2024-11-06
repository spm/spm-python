from spm.__wrapper__ import Runtime


def _getdimord(*args, **kwargs):
    """
      GETDIMORD determine the dimensions and order of a data field in a FieldTrip  
        structure.  
         
        Use as  
          dimord = getdimord(data, field)  
         
        See also GETDIMSIZ, GETDATFIELD, FIXDIMORD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/getdimord.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("getdimord", *args, **kwargs)
