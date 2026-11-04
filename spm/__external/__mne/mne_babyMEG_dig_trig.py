from spm._runtime import Runtime


def mne_babyMEG_dig_trig(*args, **kwargs):
    r"""
       
        function mne_baby_meg_dig_trig(infile,outfile,threshold,invert,want_eeg);  
         
        Read and write raw data in 60-sec blocks  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_babyMEG_dig_trig.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_baby_meg_dig_trig", *args, **kwargs, nargout=0)
