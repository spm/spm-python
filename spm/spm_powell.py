from spm._runtime import Runtime


def spm_powell(*args, **kwargs):
    r"""
      Powell optimisation method  
        FORMAT [p,f] = spm_powell(p,xi,tolsc,func,varargin)  
          p        - Starting parameter values  
          xi       - columns containing directions in which to begin searching  
          tolsc    - stopping criteria, optimisation stops when  
                       sqrt(sum(((p-p_prev)./tolsc).^2))<1  
          func     - name of evaluated function  
          varargin - remaining arguments to func (after p)  
         
          p        - final parameter estimates  
          f        - function value at minimum  
       __________________________________________________________________________  
         
        Method is based on Powell's optimisation method described in  
        Numerical Recipes (Press, Flannery, Teukolsky & Vetterling).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_powell.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_powell", *args, **kwargs)
