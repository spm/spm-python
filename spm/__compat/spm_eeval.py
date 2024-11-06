from spm.__wrapper__ import Runtime


def spm_eeval(*args, **kwargs):
    """
      Expression evaluation  
        FORMAT [p,msg] = spm_eeval(str,Type,n,m)  
        Str  - Expression to work with  
         
        Type - type of evaluation  
             - 's'tring  
             - 'e'valuated string  
                 - 'n'atural numbers  
                 - 'w'hole numbers  
                 - 'i'ntegers  
                 - 'r'eals  
             - 'c'ondition indicator vector  
         
        n ('e', 'c' & 'p' types)  
                 - Size of matrix required  
                 - NaN for 'e' type implies no checking - returns input as evaluated  
                 - length of n(:) specifies dimension - elements specify size  
                 - Inf implies no restriction  
                 - Scalar n expanded to [n,1] (i.e. a column vector)  
                   (except 'x' contrast type when it's [n,np] for np  
                 - E.g: [n,1] & [1,n] (scalar n) prompt for an n-vector,  
                                returned as column or row vector respectively  
                        [1,Inf] & [Inf,1] prompt for a single vector,  
                                returned as column or row vector respectively  
                        [n,Inf] & [Inf,n] prompts for any number of n-vectors,  
                                returned with row/column dimension n respectively.  
                        [a,b] prompts for an 2D matrix with row dimension a and  
                                column dimension b  
                        [a,Inf,b] prompt for a 3D matrix with row dimension a,  
                                page dimension b, and any column dimension.  
                 - 'c' type can only deal with single vectors  
                 - NaN for 'c' type treated as Inf  
                 - Defaults (missing or empty) to NaN  
         
        m ('n', 'w', 'n1', 'w1', 'bn1' & 'bw1' types)  
                 - Maximum value (inclusive)  
         
        m ('r' type)  
                 - Maximum and minimum values (inclusive)  
         
        m ('c' type)  
              - Number of unique conditions required by 'c' type  
                 - Inf implies no restriction  
                 - Defaults (missing or empty) to Inf - no restriction  
         
        p     - Result  
         
        msg   - Explanation of why it didn't work  
         
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_eeval.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeval", *args, **kwargs)
