from spm.__wrapper__ import Runtime


def spm_Ncdf_jdw(*args, **kwargs):
    """
      Cumulative Distribution Function (CDF) for univariate Normal distributions: J.D.  Williams approximation  
        FORMAT F = spm_Ncdf_jdw(x,u,v)  
         
        x - ordinates  
        u - mean              [Defaults to 0]  
        v - variance  (v>0)   [Defaults to 1]  
        F - pdf of N(u,v) at x (Lower tail probability)  
       __________________________________________________________________________  
         
        spm_Ncdf implements the Cumulative Distribution Function (CDF) for  
        the Normal (Gaussian) family of distributions.  
         
        References:  
       --------------------------------------------------------------------------  
        An Approximation to the Probability Integral  
        J. D. Williams   
        The Annals of Mathematical Statistics, Vol. 17, No. 3. (Sep., 1946), pp.  
        363-365.   
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Ncdf_jdw.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Ncdf_jdw", *args, **kwargs)
