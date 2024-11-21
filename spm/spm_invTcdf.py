from spm.__wrapper__ import Runtime


def spm_invTcdf(*args, **kwargs):
    """
      Inverse Cumulative Distribution Function (CDF) of Students t distribution  
        FORMAT x = spm_invTcdf(F,v)  
         
        F  - CDF (lower tail p-value)  
        v - degrees of freedom (v>0, non-integer d.f. accepted)  
        x - T-variate (Student's t has range (-Inf,Inf))  
       __________________________________________________________________________  
         
        spm_invTcdf implements the inverse Cumulative Distribution of Students  
        t-distributions.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The Student's t-distribution with v degrees of freedom is defined for  
        positive integer v and real x. The Cumulative Distribution  
        Function (CDF) F(x) is the probability that a realisation of a  
        t-distributed random variable X has value less than x. F(x)=Pr{X<x}:  
        (See Evans et al., Ch37)  
         
        This implementation is not restricted to whole (positive integer) df  
        v, rather it will compute for any df v>0.  
         
        Variate relationships: (Evans et al., Ch37 & 7)  
       --------------------------------------------------------------------------  
        The Student's t distribution with 1 degree of freedom is the Standard  
        Cauchy distribution, which has a simple closed form CDF.  
         
        For X a t-variate with v degrees of freedom, v/(v+X^2) has  
        distribution related to a Beta random variable with shape parameters  
        w/2 & 1/2, as described below.  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        Using the routine spm_invBcdf for the Beta distribution, with  
        appropriate parameters:  The CDF of the Student's t-distribution with  
        v degrees of freedom is related to the incomplete beta function by:  
              Pr(|X|<x) = betainc(v/(v+x^2),v/2,1/2)  
        so  
                     {     betainc(v/(v+x^2),v/2,1/2) / 2      for x<0  
              F(x) = |   0.5                                   for x=0  
                     { 1 - betainc(v/(v+x^2),v/2,1/2) / 2      for x>0  
         
        See Abramowitz & Stegun, 26.5.27 & 26.7.1; Press et al., Sec6.4 for  
        definitions of the incomplete beta function. The relationship is  
        easily verified by substituting for v/(v+x^2) in the integral of the  
        incomplete beta function.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_invTcdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_invTcdf", *args, **kwargs)
