from spm._runtime import Runtime


def _browse_audiovideo(*args, **kwargs):
    r"""
      BROWSE_AUDIOVIDEO reads and vizualizes the audio and/or video data  
        corresponding to the EEG/MEG data segment that is passed into this  
        function.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/browse_audiovideo.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("browse_audiovideo", *args, **kwargs, nargout=0)
