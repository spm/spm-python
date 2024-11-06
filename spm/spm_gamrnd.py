from spm.__wrapper__ import Runtime


def spm_gamrnd(*args, **kwargs):
    """
      Random arrays from gamma distribution - a compiled routine  
        FORMAT r = spm_gamrnd(a,b,m,n,...)  
         
        a        - shape parameter  
        b        - scale parameter  
        m,n,...  - dimensions of the output array [optional]  
         
        r        - array of random numbers chosen from the gamma distribution  
       __________________________________________________________________________  
         
        Reference  
          
        George Marsaglia and Wai Wan Tsang, "A Simple Method for Generating Gamma  
        Variables": ACM Transactions on Mathematical Software, Vol. 26, No. 3,  
        September 2000, Pages 363-372  
        http://portal.acm.org/citation.cfm?id=358414  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_gamrnd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gamrnd", *args, **kwargs)
