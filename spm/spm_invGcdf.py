from spm.__wrapper__ import Runtime


def spm_invGcdf(*args, **kwargs):
    """
      Inverse Cumulative Distribution Function (CDF) of Gamma distribution  
        FORMAT x = spm_invGcdf(p,h,l,tol)  
         
        F   - CDF (lower tail p-value)  
        h   - Shape parameter (h>0)  
        l   - Scale parameter (l>0)  
        x   - Gamma ordinates at which CDF F(x)=F  
        tol - tolerance [default 10^-6]  
       __________________________________________________________________________  
         
        spm_invGcdf implements the inverse Cumulative Distribution Function  
        for Gamma distributions.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The Gamma distribution has shape parameter h and scale l, and is  
        defined for h>0 & l>0 and for x in [0,Inf) (See Evans et al., Ch18,  
        but note that this reference uses the alternative parameterisation of  
        the Gamma with scale parameter c=1/l)  
         
        The Cumulative Distribution Function (CDF) F(x) is the probability  
        that a realisation of a Gamma random variable X has value less than  
        x. F(x)=Pr{X<x}:  (See Evans et al., Ch18)  
         
        Variate relationships: (Evans et al., Ch8 & Ch18)  
       --------------------------------------------------------------------------  
        For natural (strictly +ve integer) shape h this is an Erlang distribution.  
         
        The Standard Gamma distribution has a single parameter, the shape h.  
        The scale taken as l=1.  
         
        The Chi-squared distribution with v degrees of freedom is equivalent  
        to the Gamma distribution with scale parameter 1/2 and shape parameter v/2.  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        Interval bisection to find the inverse CDF to within tol.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_invGcdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_invGcdf", *args, **kwargs)
