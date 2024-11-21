from spm.__wrapper__ import Runtime


def keyvalcheck(*args, **kwargs):
    """
      KEYVALCHECK is a helper function for parsing optional key-value input pairs.  
         
        Use as  
          keyvalcheck(argin, 'required',  {'key1', 'key2', ...})  
          keyvalcheck(argin, 'forbidden', {'key1', 'key2', ...})  
          keyvalcheck(argin, 'optional',  {'key1', 'key2', ...})  
         
        See also KEYVAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/keyvalcheck.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("keyvalcheck", *args, **kwargs, nargout=0)
