from spm.__wrapper__ import Runtime


def spm_eeg_ft_artefact_visual(*args, **kwargs):
    """
      Function for interactive artefact rejection using Fieldtrip  
         
        Disclaimer: this code is provided as an example and is not guaranteed to work  
        with data on which it was not tested. If it does not work for you, feel  
        free to improve it and contribute your improvements to the MEEGtools toolbox  
        in SPM (http://www.fil.ion.ucl.ac.uk/spm)  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_ft_artefact_visual.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_ft_artefact_visual", *args, **kwargs)
