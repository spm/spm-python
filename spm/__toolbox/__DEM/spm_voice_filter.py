from spm.__wrapper__ import Runtime


def spm_voice_filter(*args, **kwargs):
    """
      Time frequency decomposition to characterise acoustic spectral envelope  
        FORMAT [G,F0] = spm_voice_filter(Y,FS)  
         
        Y    - timeseries  
        FS   - sampling frequency  
        F1   - lower frequency bound [default: 1024  Hz]  
        F2   - upper frequency bound [default: 16096 Hz]  
         
        G    - power at acoutic frequencies  
        F0   - fundamental frequency  
         
        This auxiliary routine uses a wavelet decomposition (complex Gaussian wavelets) to  
        assess the power frequency range (F1 - F2 Hz). This can be used to  
        identify the onset of a word or fast modulations of spectral energy at a  
        fundamental frequency F0 of 256 Hz.  
         
        This routine is not used for voice recognition but can be useful for  
        diagnostics and plotting spectral envelope.  
         
        see also: spm_voice_check.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_filter.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_filter", *args, **kwargs)
