from spm.__wrapper__ import Runtime


def mne_source_spectral_analysis(*args, **kwargs):
    """
       
        [res] = mne_source_spectral_analysis(fname_rawdata, fname_output, cfg)  
         
        Estimate frequency spectra in the source space and optionally write out  
        stc files which have frequencies along the "time" axis.  
         
        fname_data     - Name of the data file  
         
        MNE inversion  
        cfg.inv        - Inverse operator structure or file name  
        cfg.lambda2    - The regularization factor  
        cfg.dSPM       - enable dSPM: 0 or 1  
         
        Spectral estimation  
        cfg.mode       - output quantity; 'amplitude', 'power', 'phase'  
        cfg.window     - window type: 'hanning', 'hamming' or any other window  
                         function available on Matlab  
        cfg.fft_length - FFT length in samples (half-overlapping windows used)  
        cfg.foi        - Frequencies of interest as [f_min f_max]  
         
        Output  
        cfg.outfile    - The stem of the output STC file name holding the spectra  
         
        (C)opyright Lauri Parkkonen, 2012  
         
        $Log$  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_source_spectral_analysis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_source_spectral_analysis", *args, **kwargs)
