from spm._runtime import Runtime


def spm_EC_density(*args, **kwargs):
    r"""
      Returns the Euler characteristic (EC) density  
        FORMAT function [EC] = spm_EC_density(STAT,t,df,[D])  
         
        STAT  = 'Z','T','F',...  
        t     = vector of statistical values  
        df    = degrees of freedom [df1,df2]  
        D     = dimension of SPM [default: 4]  
         
        This routine returns the density of the expected Euler characteristic for  
        a variety of commonly used statistics. It is based upon a generic  
        expression for fields of the F statistic. This provides estimates for  
        special cases: for example, with infinite degrees of freedom of the  
        denominator, the F statistic behaves as a chi-squared statistic.  
        Similarly, when the degrees of freedom of the numerator reduce to 1, the  
        squared T statistic behaves as an F statistic. And as a Z statistic,  
        when the denominator degrees of freedom tend to infinity.  
         
        This routine returns densities over any arbitrary number of dimensions,  
        D. The default is D = 4 dimensions returning a D + 1 densities, where the  
        first corresponds to the zeroth dimension or point (i.e., using the usual  
        cumulative density for the statistic in question).  
         
        The current implementation is based upon an optimised functional form in  
        Appendix B of Worsley et al (2004). The (polynomial) summations are  
        grouped in a way to maximise efficiency. The gamma functions are  
        evaluated in log space. This enables evaluation with very high degrees of  
        freedom (with an enforced upper bound of 256).  
       __________________________________________________________________________  
         
        Reference : K.J. Worsley et al. / NeuroImage 23 (2004) S189–S195  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_EC_density.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_EC_density", *args, **kwargs)
