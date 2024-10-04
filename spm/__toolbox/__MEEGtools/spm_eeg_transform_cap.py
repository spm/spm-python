from spm.__wrap__ import _Runtime


def spm_eeg_transform_cap(*args, **kwargs):
  """  Transform an electrode cap to match the subject's headshape  
    FORMAT shape = spm_eeg_transform_cap(S)  
     
    S                    - input structure (optional)  
    (optional) fields of S:  
      S.standard         - headshape (file) with the standard locations  
      S.custom           - headshape (file) with individually measured locations  
      S.outfile          - file name to save the output                       
     
    Output:  
      sens               - transformed sensors  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_transform_cap.m)
  """

  return _Runtime.call("spm_eeg_transform_cap", *args, **kwargs)
