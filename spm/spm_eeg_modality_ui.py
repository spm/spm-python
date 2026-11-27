from spm._runtime import Runtime


def spm_eeg_modality_ui(*args, **kwargs):
    r"""
      Attempt to determine the main modality of an MEEG object.  
        If confused, asks the user.  
         
        FORMAT [mod, chanind]  = spm_eeg_modality_ui(D, scalp, planar)  
         
        D          - MEEG object  
        scalp      - only look at scalp modalities [default: false]  
        planar     - distinguish between MEG planar and other MEG types [default: false]  
         
        modality   - the chosen modality  
        chanind    - indices of the corresponding channels  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_modality_ui.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_modality_ui", *args, **kwargs)
