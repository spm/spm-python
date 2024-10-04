from spm.__wrap__ import _Runtime


def spm_DFP_plot(*args, **kwargs):
  """  Plot particles for spm_DFP  
    FORMAT spm_DFP_plot(QU,Nt)  
    FORMAT spm_DFP_plot(QU,pU)  
   --------------------------------------------------------------------------  
    QU{t}(p).x{d}  - ensemble of hidden states  
    QU{t}(p).v{d}  - ensemble of causal states  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_DFP_plot.m)
  """

  return _Runtime.call("spm_DFP_plot", *args, **kwargs, nargout=0)
