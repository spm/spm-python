from spm.__wrapper__ import Runtime


def spm_check_results(*args, **kwargs):
  """  Display several MIPs in the same figure  
    FORMAT spm_check_results(SPMs,xSPM)  
    SPMs    - char or cell array of paths to SPM.mat[s]  
    xSPM    - structure containing thresholding details, see spm_getSPM.m  
     
    Beware: syntax and features of this function are likely to change.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_check_results.m)
  """

  return Runtime.call("spm_check_results", *args, **kwargs, nargout=0)
