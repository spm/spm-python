from spm._runtime import Runtime


def spm_Gcdf(*args, **kwargs):
    """
      Cumulative Distribution Function (CDF) of Gamma distribution  
        FORMAT F = spm_Gcdf(x,h,l,tail)  
         
        x    - Gamma-variate   (Gamma has range [0,Inf) )  
        h    - Shape parameter (h>0)  
        l    - Scale parameter (l>0)  
        tail - if 'upper', return the upper tail probability of the Gamma  
               distribution [Default: 'lower']  
        F    - CDF of Gamma-distribution with shape & scale parameters h & l  
       __________________________________________________________________________  
         
        spm_Gcdf implements the Cumulative Distribution of the Gamma-distribution.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The CDF F(x) of the Gamma distribution with shape parameter h and  
        scale l is the probability that a realisation of a Gamma random  
        variable X has value less than x F(x)=Pr{X<x} for X~G(h,l). The Gamma  
        distribution is defined for h>0 & l>0 and for x in [0,Inf) (See Evans  
        et al., Ch18, but note that this reference uses the alternative  
        parameterisation of the Gamma with scale parameter c=1/l)  
         
        Variate relationships: (Evans et al., Ch18 & Ch8)  
       --------------------------------------------------------------------------  
        For natural (strictly +ve integer) shape h this is an Erlang distribution.  
         
        The Standard Gamma distribution has a single parameter, the shape h.  
        The scale taken as l=1.  
         
        The Chi-squared distribution with v degrees of freedom is equivalent  
        to the Gamma distribution with scale parameter 1/2 and shape parameter v/2.  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        The CDF of the Gamma distribution with scale parameter l and shape h  
        is related to the incomplete Gamma function by  
         
              F(x) = gammainc(l*x,h)  
         
        See Abramowitz & Stegun, 6.5.1; Press et al., Sec6.2 for definitions  
        of the incomplete Gamma function. The relationship is easily verified  
        by substituting for t/c in the integral, where c=1/l.  
         
        MATLAB's implementation of the incomplete gamma function is used.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Gcdf.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_Gcdf", *args, **kwargs)
