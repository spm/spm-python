from spm.__wrapper__ import Runtime


def spm_Fpdf(*args, **kwargs):
    """
      Probability Density Function (PDF) of F (Fisher-Snedecor) distribution  
        FORMAT f = spm_Fpdf(x,df)  
        FORMAT f = spm_Fpdf(x,v,w)  
         
        x  - F-variate   (F has range [0,Inf) )  
        df - Degrees of freedom, concatenated along last dimension  
             Eg. Scalar (or column vector) v & w. Then df=[v,w];  
        v  - Shape parameter 1 /   numerator degrees of freedom (v>0)  
        w  - Shape parameter 2 / denominator degrees of freedom (w>0)  
        f  - PDF of F-distribution with [v,w] degrees of freedom at points x  
       __________________________________________________________________________  
         
        spm_Fpdf implements the Probability Density Function of the F-distribution.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The PDF of the F-distribution with degrees of freedom v & w, defined  
        for positive integer degrees of freedom v>0 & w>0, and for x in  
        [0,Inf) by: (See Evans et al., Ch16)  
         
                    gamma((v+w)/2)  * (v/w)^(v/2) x^(v/2-1)  
           f(x) = --------------------------------------------  
                  gamma(v/2)*gamma(w/2) * (1+(v/w)x)^((v+w)/2)  
         
        Variate relationships: (Evans et al., Ch16 & 37)  
       --------------------------------------------------------------------------  
        The square of a Student's t variate with w degrees of freedom is  
        distributed as an F-distribution with [1,w] degrees of freedom.  
         
        For X an F-variate with v,w degrees of freedom, w/(w+v*X^2) has  
        distributed related to a Beta random variable with shape parameters  
        w/2 & v/2.  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        Direct computation using the beta function for  
              gamma(v/2)*gamma(w/2) / gamma((v+w)/2)  =  beta(v/2,w/2)  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Fpdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Fpdf", *args, **kwargs)
