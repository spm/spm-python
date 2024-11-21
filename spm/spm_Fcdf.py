from spm.__wrapper__ import Runtime


def spm_Fcdf(*args, **kwargs):
    """
      Cumulative Distribution Function (CDF) of F (Fisher-Snedecor) distribution  
        FORMAT F = spm_Fcdf(x,df)  
        FORMAT F = spm_Fcdf(x,v,w)  
         
        x  - F-variate   (F has range [0,Inf) )  
        df - Degrees of freedom, concatenated along last dimension  
             Eg. Scalar (or column vector) v & w. Then df=[v,w];  
        v  - Shape parameter 1 /   numerator degrees of freedom (v>0)  
        w  - Shape parameter 2 / denominator degrees of freedom (w>0)  
        F  - CDF of F-distribution with [v,w] degrees of freedom at points x  
       __________________________________________________________________________  
         
        spm_Fcdf implements the Cumulative Distribution Function of the F-distribution.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The CDF F(x) of the F distribution with degrees of freedom v & w,  
        defined for positive integer degrees of freedom v & w, is the  
        probability that a realisation of an F random variable X has value  
        less than x F(x)=Pr{X<x} for X~F(v,w). The F-distribution is defined  
        for v>0 & w>0, and for x in [0,Inf) (See Evans et al., Ch16).  
         
        Variate relationships: (Evans et al., Ch16 & 37)  
       --------------------------------------------------------------------------  
        The square of a Student's t variate with w degrees of freedom is  
        distributed as an F-distribution with [1,w] degrees of freedom.  
         
        For X an F-variate with v,w degrees of freedom, w/(w+v*X^2) has  
        distributed related to a Beta random variable with shape parameters  
        w/2 & v/2.  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        Using the relationship with the Beta distribution: The CDF of the  
        F-distribution with v,w degrees of freedom is related to the  
        incomplete beta function by:  
              Pr(X<x) = 1 - betainc(w/(w+v*x^2),w/2,v/2)  
        See Abramowitz & Stegun, 26.6.2; Press et al., Sec6.4 for  
        definitions of the incomplete beta function. The relationship is  
        easily verified by substituting for w/(w+v*x^2) in the integral of the  
        incomplete beta function.  
         
        MATLAB's implementation of the incomplete beta function is used.  
         
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Fcdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Fcdf", *args, **kwargs)
