from spm.__wrapper__ import Runtime


def spm_cat(*args, **kwargs):
    """
      Convert a cell array into a matrix - a compiled routine  
        FORMAT [x] = spm_cat(x,d)  
        x - cell array  
        d - dimension over which to concatenate [default - both]  
       __________________________________________________________________________  
        Empty array elements are replaced by sparse zero partitions and single 0  
        entries are expanded to conform to the non-empty non zero elements.  
         
        e.g.:  
        > x       = spm_cat({eye(2) []; 0 [1 1; 1 1]})  
        > full(x) =  
         
            1     0     0     0  
            0     1     0     0  
            0     0     1     1  
            0     0     1     1  
         
        If called with a dimension argument, a cell array is returned.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_cat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cat", *args, **kwargs)
