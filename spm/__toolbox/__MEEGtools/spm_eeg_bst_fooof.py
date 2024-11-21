from spm.__wrapper__ import Runtime


def spm_eeg_bst_fooof(*args, **kwargs):
    """
      Remove the aperiodic component from the spectrum using the FOOOF algorithm  
        Donoghue et al. (2020). Nature Neuroscience, 23, 1655-1665.  
         
        This uses the Brainstorm implementation by Luc Wilson  
         
        FORMAT  D = spm_eeg_bst_fooof(S)  
         
        S         - struct (optional)  
        (optional) fields of S:  
        S.D - meeg object, filename or a list of filenames of SPM EEG files  
        S.freq_range        - frequency range for fitting  
        S.peak_width_limits - how wide the peaks can be  
        S.max_peaks         - maximal number of peaks  
        S.min_peak_height   - minimal peak height  
        S.aperiodic_mode    - shape of the aperiodic component fixed|knee%  
        S.peak_threshold    - threshold for detecting a peak  
        S.peak_type         - Shape of the peak fit best|gaussian|cauchy  
        S.line_noise_freq   - Line noise frequency 50|60Hz  
        S.line_noise_width  - range around line noise peaks to interpolate  
        S.guess_weight      - Parameter to weigh initial estimates during  
                              optimization none|weak|strong  
        S.proximity_threshold  -  threshold to remove the smallest of two peaks  
                                  if too close  
         
        Output:  
        D         - MEEG data struct with FOOOF-corrected spectra  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_bst_fooof.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_bst_fooof", *args, **kwargs)
