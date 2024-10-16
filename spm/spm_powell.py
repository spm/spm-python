from spm.__wrapper__ import Runtime


def spm_powell(*args, **kwargs):
  """  Powell optimisation method  
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
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_powell.m)
  """

  return Runtime.call("spm_powell", *args, **kwargs)
