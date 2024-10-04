from spm.__wrap__ import _Runtime


def spm_eeg_modality_ui(*args, **kwargs):
  """  Attempt to determine the main modality of an MEEG object.  
    If confused, asks the user.  
     
    FORMAT [mod, chanind]  = spm_eeg_modality_ui(D, scalp, planar)  
     
    D          - MEEG object  
    scalp      - only look at scalp modalities [default: false]  
    planar     - distinguish between MEG planar and other MEG types [default: false]  
     
    modality   - the chosen modality  
    chanind    - indices of the corresponding channels  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_modality_ui.m)
  """

  return _Runtime.call("spm_eeg_modality_ui", *args, **kwargs)
