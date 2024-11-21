from spm.__wrapper__ import Runtime


def spm_type(*args, **kwargs):
    """
      Translate data type specifiers between SPM & MATLAB representations  
        FORMAT T = spm_type(x, arg)  
        x    - specifier  
        T    - type  
        arg  - optional string argument, can be:  
                - 'maxval'  - return maximum allowed value.  
                - 'minval'  - return minimum allowed value.  
                - 'nanrep'  - return 1 if there is a NaN representation.  
                - 'bits'    - return the number of bits per voxel.  
                - 'intt'    - return 1 if values rounded to nearest integer.  
                - 'conv'    - return conversion function handle.  
       __________________________________________________________________________  
         
        Format specifiers are based on NIFTI-1.  
        If the input is a number then the corresponding MATLAB string is  
        returned by default.  
        If the input is a string then the appropriate TYPE is returned.  
        However, if the optional arg argument is supplied then other  
        information will be returned instead.  
         
        With no arguments, a list of data types is returned.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_type.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_type", *args, **kwargs)
