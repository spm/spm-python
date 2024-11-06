from spm.__wrapper__ import Runtime


def ft_audiovideobrowser(*args, **kwargs):
    """
      FT_AUDIOVIDEOBROWSER reads and vizualizes the audio and/or video data  
        corresponding to the EEG/MEG data that is passed into this function.  
         
        Use as  
          ft_audiovideobrowser(cfg)  
        or as  
          ft_audiovideobrowser(cfg, data)  
        where the input data is the result from FT_PREPROCESSING or from FT_COMPONENTANALYSIS.  
         
        The configuration structure can contain the following options  
          cfg.datahdr     = header structure of the EEG/MEG data, see FT_READ_HEADER  
          cfg.audiohdr    = header structure of the audio data, see FT_READ_HEADER  
          cfg.videohdr    = header structure of the video data, see FT_READ_HEADER  
          cfg.audiofile   = string with the filename  
          cfg.videofile   = string with the filename  
          cfg.trl         = Nx3 matrix, expressed in the MEG/EEG data samples, see FT_DEFINETRIAL  
          cfg.anonymize   = [x1 x2 y1 y2], range in pixels for placing a bar over the eyes (default = [])  
          cfg.interactive = 'yes' or 'no' (default = 'yes')  
         
        If you do NOT specify cfg.datahdr, the header must be present in the input data.  
        If you do NOT specify cfg.audiohdr, the header will be read from the audio file.  
        If you do NOT specify cfg.videohdr, the header will be read from the video file.  
        If you do NOT specify cfg.trl, the input data should contain a sampleinfo field.  
         
        See also FT_DATABROWSER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_audiovideobrowser.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_audiovideobrowser", *args, **kwargs, nargout=0)
