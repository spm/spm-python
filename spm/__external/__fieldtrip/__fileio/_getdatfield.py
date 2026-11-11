from spm._runtime import Runtime


def _getdatfield(*args, **kwargs):
    r"""
      GETDATFIELD  
         
        Use as  
          [datfield, dimord] = getdatfield(data)  
        where the output arguments are cell-arrays.  
         
        See also GETDIMORD, GETDIMSIZ  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/getdatfield.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getdatfield", *args, **kwargs)
