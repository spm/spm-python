from spm._runtime import Runtime


def _fixname(*args, **kwargs):
    """
      FIXNAME changes all inappropriate characters in a string into '_'  
        so that it can be used as a filename or as a field name in a structure.  
        If the string begins with a digit, an 'x' is prepended.  
         
        Use as  
          str = fixname(str)  
         
        MATLAB 2014a introduces the matlab.lang.makeValidName and  
        matlab.lang.makeUniqueStrings functions for constructing unique  
        identifiers, but this particular implementation also works with  
        older MATLAB versions.  
         
        See also DEBLANK, STRIP, PAD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/fixname.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixname", *args, **kwargs)
