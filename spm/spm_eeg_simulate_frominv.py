from spm._runtime import Runtime


def spm_eeg_simulate_frominv(*args, **kwargs):
    r"""
      Project a source inversion solution back out to the sensor level plus some noise  
        FORMAT [Dnew] = spm_eeg_simulate_frominv(D,prefix,val,whitenoise,SNRdB,trialind)  
        D          - original dataset  
        prefix     - prefix of new dataset  
        val        - use solution (and lead fields) corresponding to this index  
        whitenoise - total rms white noise in Tesla  
        SNRdB      - SNR in dBs (alternative to specifying white noise)  
        trialind   - trials in which the simulated signal is to appear  
                     (all other trials will be noise)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_simulate_frominv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_simulate_frominv", *args, **kwargs)
