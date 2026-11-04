from spm._runtime import Runtime


def spm_funfun(*args, **kwargs):
    r"""
      Utility function to evaluate functionals  
        FORMAT [F] = spm_funfun({f1,x11,x12,..f2,x22,...)  
         
        F     = f ... f2(f1(x11,x12,...),x22,...)) ... )  
         
        e.g. spm_funfun(@(x) cos(x),2.1,@(x,a) x^a,2)  
         
        which is cos(2.1)^2  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_funfun.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_funfun", *args, **kwargs)
