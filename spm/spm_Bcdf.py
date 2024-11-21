from spm.__wrapper__ import Runtime


def spm_Bcdf(*args, **kwargs):
    """
      Inverse Cumulative Distribution Function (CDF) of Beta distribution  
        FORMAT F = spm_Bcdf(x,v,w)  
         
        x   - Beta variates (Beta has range [0,1])  
        v   - Shape parameter (v>0)  
        w   - Shape parameter (w>0)  
        F   - CDF of Beta distribution with shape parameters [v,w] at points x  
       __________________________________________________________________________  
         
        spm_Bcdf implements the Cumulative Distribution Function for Beta  
        distributions.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The Beta distribution has two shape parameters, v and w, and is  
        defined for v>0 & w>0 and for x in [0,1] (See Evans et al., Ch5).  
        The Cumulative Distribution Function (CDF) F(x) is the probability  
        that a realisation of a Beta random variable X has value less than  
        x. F(x)=Pr{X<x}: This function is usually known as the incomplete Beta  
        function. See Abramowitz & Stegun, 26.5; Press et al., Sec6.4 for  
        definitions of the incomplete beta function.  
         
        Variate relationships:  
       --------------------------------------------------------------------------  
        Many: See Evans et al., Ch5  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        Using MATLAB's implementation of the incomplete beta finction (betainc).  
         
        References:  
       --------------------------------------------------------------------------  
        Evans M, Hastings N, Peacock B (1993)  
              "Statistical Distributions"  
               2nd Ed. Wiley, New York  
         
        Abramowitz M, Stegun IA, (1964)  
              "Handbook of Mathematical Functions"  
               US Government Printing Office  
         
        Press WH, Teukolsky SA, Vetterling AT, Flannery BP (1992)  
              "Numerical Recipes in C"  
               Cambridge  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Bcdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Bcdf", *args, **kwargs)
