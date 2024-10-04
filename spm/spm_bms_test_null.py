from spm.__wrap__ import _Runtime


def spm_bms_test_null(*args, **kwargs):
  """  Plot PPM showing evidence for null  
    FORMAT spm_bms_test_null(logbf_file)  
     
    logbf_file  -  Log Bayes Factor file providing evidence against null  
     
    Call this function when SPM is already running  
    or set SPM to appropriate modality eg. spm('defaults','FMRI');  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_bms_test_null.m)
  """

  return _Runtime.call("spm_bms_test_null", *args, **kwargs, nargout=0)
