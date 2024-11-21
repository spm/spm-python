from spm.__wrapper__ import Runtime


def spm_funfun(*args, **kwargs):
    """
      Utility function to evaluate functionals  
        FORMAT [F] = spm_funfun({f1,x11,x12,..f2,x22,...)  
         
        F     = f ... f2(f1(x11,x12,...),x22,...)) ... )  
         
        e.g. spm_funfun(@(x) cos(x),2.1,@(x,a) x^a,2)  
         
        which is cos(2.1)^2  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_funfun.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_funfun", *args, **kwargs)
