from spm.__wrapper__ import Runtime


def spm_dctdst(*args, **kwargs):
    """
      Function pointers to various forms of sin and cosine transforms etc  
        FORMAT fun = spm_dctdst  
        fun - a structure with function handles  
         
        Multidimensional transforms  
        FORMAT G = fun.function(F)  
        where function can be:  
        dct2n  - Multidimensional type II discrete cosine transform  
        idct2n - Multidimensional inverse type II discrete cosine transform  
        dst1n  - Multidimensional type I discrete sin transform  
        idst1n - Multidimensional inverse type I discrete sin transform  
        dst2n  - Multidimensional type II discrete sin transform  
        idst2n - Multidimensional inverse type II discrete sin transform  
         
        One dimensional transforms of columns  
        FORMAT G = fun.function(F)  
        where function can be:  
        dct2   - Type II discrete cosine transform  
        idct2  - Inverse type II discrete cosine transform  
        dst1   - Type I discrete sin transform  
        idst1  - Inverse type I discrete sin transform  
        dst2   - Type II discrete sin transform  
        idst2  - Inverse type II discrete sin transform  
         
        FORMAT A = fun.permute2mat(B,dim)  
        B      - Multidimensional array  
        dim    - Dimension to put into the columns  
        A      - Matrix of re-arranged values  
         
        FORMAT B = fun.permute2vol(A,dim,d)  
        A      - Matrix of re-arranged values  
        dim    - Dimension of multidimensional array  
                 corresponding with columns of A  
        d      - Dimensions of multidimensional array  
        B      - Multidimensional array  
         
       __________________________________________________________________________  
         
        Code works only for real data. Note that it is still a work in progress,  
        so is likely to change considerably.  
        Some functions remain undocumented for now.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_dctdst.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dctdst", *args, **kwargs)
