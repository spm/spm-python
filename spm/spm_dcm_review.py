from spm.__wrapper__ import Runtime


def spm_dcm_review(*args, **kwargs):
  """  Review an estimated DCM  
    FORMAT spm_dcm_review(DCM,action)  
     
    DCM    - DCM structure or its filename  
    action - one of:  
             'fixed connections'  
             ['    effects of ' DCM.U.name{i}];  
             'contrast of connections'  
             'location of regions'  
             'inputs'  
             'outputs'  
             'kernels'  
             'estimates of states'  
             'estimates of parameters'  
             'estimates of precisions'  
             ['   hidden states: ' DCM.Y.name{i}]  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_review.m)
  """

  return Runtime.call("spm_dcm_review", *args, **kwargs, nargout=0)
