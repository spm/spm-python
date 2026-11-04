from spm._runtime import Runtime


def _keyvalcheck(*args, **kwargs):
    r"""
      KEYVALCHECK is a helper function for parsing optional key-value input pairs.  
         
        Use as  
          keyvalcheck(argin, 'required',  {'key1', 'key2', ...})  
          keyvalcheck(argin, 'forbidden', {'key1', 'key2', ...})  
          keyvalcheck(argin, 'optional',  {'key1', 'key2', ...})  
         
        See also KEYVAL  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/specest/private/keyvalcheck.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("keyvalcheck", *args, **kwargs, nargout=0)
