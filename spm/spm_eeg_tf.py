from spm.__wrapper__ import Runtime


def spm_eeg_tf(*args, **kwargs):
    """
      Compute instantaneous power and phase in peri-stimulus time and frequency  
        FORMAT [Dtf, Dtph] = spm_eeg_tf(S)  
         
        S                     - input structure  
         
        fields of S:  
          S.D                 - MEEG object or filename of M/EEG mat-file with  
         
          S.channels          - cell array of channel names. Can include generic  
                                wildcards: 'All', 'EEG', 'MEG' etc.  
         
          S.frequencies      - vector of frequencies of interest  
         
          S.timewin          - time window of interest in PST in ms.  
         
          S.method           - name for the spectral estimation to use. This  
                               corresponds to the name of a plug-in function that comes  
                               after 'spm_eeg_specest_' prefix.  
          S.settings         - plug-in specific settings  
         
          S.phase            - also save phase dataset (1) or not (0)  
                               phase dataset cannot be computed for some  
                               spectral estimation methods  
          S.prefix           - prefix added before the standard prefix (tf_ or tph_)  
         
        Output:  
        Dtf                   - M/EEG object with power (also written on disk)  
        Dtph                  - M/EEG object with phase (also written on disk)  
       __________________________________________________________________________  
        This is a modular function for which plugins can be developed implementing  
        specific spectral estimation methods. There are 3 basic plugins presently  
        implemented and they can be used as templates for new plugins.  
        The name of a plugin function should start with 'spm_eeg_specest_'  
         
        morlet (spm_eeg_specest_morlet) - Morlet wavelet transform  
         
        hilbert (spm_eeg_specest_hilbert) - filtering + Hilbert transform  
         
        ft_mtmconvol (spm_eeg_specest_mtmconvol) - Fieldtrip implementation  
                                                  of multi-taper spectral  
                                                  analysis  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_tf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_tf", *args, **kwargs)
