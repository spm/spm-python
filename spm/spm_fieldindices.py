from spm.__wrapper__ import Runtime


def spm_fieldindices(*args, **kwargs):
    """
      Return the indices of fields in a structure (and vice versa)  
        FORMAT [i]     = spm_fieldindices(X,field1,field2,...)  
        FORMAT [field] = spm_fieldindices(X,i)  
         
        X         - structure  
        field1,.. - fields  
         
        i         - vector of indices or fieldname{s}  
         
        Note: Fields are returned in column order of X, regardless of the order  
        of fields specified in the input.  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fieldindices.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fieldindices", *args, **kwargs)
