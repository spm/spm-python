from spm.__wrapper__ import Runtime


def spm_dcm_generate(*args, **kwargs):
    """
      Generate synthetic data from a DCM specification  
        FORMAT [Y,x,DCM] = spm_dcm_generate(syn_model,SNR,show_graphics)  
          
        syn_model     - Name of synthetic DCM file  
        SNR           - Signal to noise ratio [default: 1]  
        show_graphics - Whether to plot each timeseries [default: true]  
         
        This routine will update the DCM.Y field as follows:   
                  Y.y    - synthetic BOLD data  
                  Y.secs - overall number of seconds  
                  Y.Q    - components of error precision  
         
        and will enter neuronal activity (first hidden var in each region) into   
        DCM.x  
         
        Y           - Simulated (Noisy) BOLD data  
        x           - Simulated neuronal activity (first hidden variable in each region)  
        DCM         - Full generative model  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_generate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_generate", *args, **kwargs)
