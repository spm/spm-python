from spm.__wrapper__ import Runtime


def _getdatfield(*args, **kwargs):
    """
      GETDATFIELD  
         
        Use as  
          [datfield, dimord] = getdatfield(data)  
        where the output arguments are cell-arrays.  
         
        See also GETDIMORD, GETDIMSIZ  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/getdatfield.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("getdatfield", *args, **kwargs)
