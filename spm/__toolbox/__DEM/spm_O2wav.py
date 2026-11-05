from spm._runtime import Runtime


def spm_O2wav(*args, **kwargs):
    r"""
      O to WAV image format  
        FORMAT wav = spm_O2wav(O,WAV)  
         
        Converts discrete (probabilistic) image into an WAV format for sonogram  
        [dis]play.  
         
        This routine generates an image using spatiotemporal basis functions  
        weighted by expected singular variance; where the requisite expectations  
        are evaluated over discrete values, given a multinomial distribution over  
        those values. This routine is specialised for one-dimensional timeseries;  
        e.g., time frequency or sonogram representation of audio files.  
         
        see also: spm_wav2O and spm_O2rgb  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_O2wav.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_O2wav", *args, **kwargs)
