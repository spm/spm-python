from spm.__wrapper__ import Runtime


def spm_DEM_qU(*args, **kwargs):
  """  Display conditional estimates of states (qU)  
    FORMAT spm_DEM_qU(qU,pU)  
     
    qU.v{i}    - causal states (V{1} = y = predicted response)  
    qU.x{i}    - hidden states  
    qU.e{i}    - prediction error  
    qU.C{N}    - conditional covariance - [causal states] for N samples  
    qU.S{N}    - conditional covariance - [hidden states] for N samples  
     
    pU         - optional input for known states  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_DEM_qU.m)
  """

  return Runtime.call("spm_DEM_qU", *args, **kwargs, nargout=0)
