from spm._runtime import Runtime


def spm_voice_repeat(*args, **kwargs):
    r"""
      Illustrates voice recognition  
        FORMAT spm_voice_repeat  
         
        When invoked, this routine takes an audio input to estimate the  
        fundamental and formant frequencies of the speaker. It will then plot the  
        estimates and segment a short sentence. The sentence can be replayed  
        after being recognised, with and without lexical content and prosody.  
        this routinely uses dialogue boxes to step through the various  
        demonstrations.  
         
        See also: spm_voice_speak.m and spm_voice_segmentation.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_voice_repeat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_voice_repeat", *args, **kwargs, nargout=0)
