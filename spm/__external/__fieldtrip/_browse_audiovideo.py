from spm.__wrapper__ import Runtime


def _browse_audiovideo(*args, **kwargs):
    """
      BROWSE_AUDIOVIDEO reads and vizualizes the audio and/or video data  
        corresponding to the EEG/MEG data segment that is passed into this  
        function.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/browse_audiovideo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("browse_audiovideo", *args, **kwargs, nargout=0)
