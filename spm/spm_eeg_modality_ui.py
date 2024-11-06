from spm.__wrapper__ import Runtime


def spm_eeg_modality_ui(*args, **kwargs):
    """
      Attempt to determine the main modality of an MEEG object.  
        If confused, asks the user.  
         
        FORMAT [mod, chanind]  = spm_eeg_modality_ui(D, scalp, planar)  
         
        D          - MEEG object  
        scalp      - only look at scalp modalities [default: false]  
        planar     - distinguish between MEG planar and other MEG types [default: false]  
         
        modality   - the chosen modality  
        chanind    - indices of the corresponding channels  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_modality_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_modality_ui", *args, **kwargs)
