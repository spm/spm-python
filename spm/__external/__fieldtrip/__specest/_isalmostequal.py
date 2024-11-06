from spm.__wrapper__ import Runtime


def _isalmostequal(*args, **kwargs):
    """
      ISALMOSTEQUAL compares two input variables and returns true/false  
        and a message containing the details on the observed difference.  
         
        Use as  
          [ok, message] = isalmostequal(a, b)  
          [ok, message] = isalmostequal(a, b, ...)  
         
        This works for all possible input variables a and b, like  
        numerical arrays, string arrays, cell arrays, structures  
        and nested data types.  
         
        Optional input arguments come in key-value pairs, supported are  
          'depth'      number, for nested structures  
          'abstol'     number, absolute tolerance for numerical comparison  
          'reltol'     number, relative tolerance for numerical comparison  
          'diffabs'    boolean, check difference between absolute values for numericals (useful for e.g. mixing matrices which have arbitrary signs)  
         
        See also ISEQUAL, ISEQUALNAN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/private/isalmostequal.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("isalmostequal", *args, **kwargs)
