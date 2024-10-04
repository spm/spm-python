from spm.__wrap__ import _Runtime


def spm_dcm_peb_review(*args, **kwargs):
  """  Review tool for DCM PEB models  
    FORMAT spm_dcm_peb_review(PEB,DCM)  
     
    PEB - PEB model to review  
    DCM - (Optional) A single DCM or cell array of DCMs. Data is used to   
          enhance the GUI.  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_peb_review.m)
  """

  return _Runtime.call("spm_dcm_peb_review", *args, **kwargs, nargout=0)
