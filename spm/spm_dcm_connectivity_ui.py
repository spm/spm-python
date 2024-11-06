from spm.__wrapper__ import Runtime


def spm_dcm_connectivity_ui(*args, **kwargs):
    """
      GUI for manually specifying connection values in a DCM  
        FORMAT con = spm_dcm_connectivity_ui(DCM,D,title_text,defaults,enabled)  
         
        DCM        - DCM structure  
        D          - 'A','B' or 'C' i.e. connectivity matrix of interest  
        title_text - Text to display above the matrix, e.g. 'Enter contrast for '  
        defaults   - (optional) structure of default values containing  
                     defaults.A, defaults.B and defaults.C  
        enabled    - (optional) structure of inputs to enable with binary   
                     matrices enabled.A, enabled.B and enabled.C  
          
        Returns:  
        con        - structure with con.A, con.B and con.C of user-entered values  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_connectivity_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_connectivity_ui", *args, **kwargs)
