from spm.__wrapper__ import Runtime


def ft_artifact_clip(*args, **kwargs):
    """
      FT_ARTIFACT_CLIP scans the data segments of interest for channels that clip, i.,e.  
        channels that have a constant value for a prolonged time, often indicating that the  
        signal was outside the range for the amplifier. These clipping artifacts are  
        detected by the signal being completely flat for a given amount of time.  
         
        Use as  
          [cfg, artifact] = ft_artifact_clip(cfg)  
        with the configuration options  
          cfg.dataset     = string with the filename  
        or  
          cfg.headerfile  = string with the filename  
          cfg.datafile    = string with the filename  
        and optionally  
          cfg.headerformat  
          cfg.dataformat  
         
        Alternatively you can use it as  
          [cfg, artifact] = ft_artifact_clip(cfg, data)  
        where the input data is a structure as obtained from FT_PREPROCESSING.  
         
        In both cases the configuration should also contain  
          cfg.trl         = structure that defines the data segments of interest, see FT_DEFINETRIAL  
          cfg.continuous  = 'yes' or 'no' whether the file contains continuous data (default is automatic)  
        and  
          cfg.artfctdef.clip.channel       = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details  
          cfg.artfctdef.clip.pretim        = pre-artifact rejection interval in seconds (default = 0)  
          cfg.artfctdef.clip.psttim        = post-artifact rejection interval in seconds (default = 0)  
          cfg.artfctdef.clip.timethreshold = number, minimum duration in seconds of a segment with consecutive identical samples to be considered as 'clipped'  
          cfg.artfctdef.clip.amplthreshold = number, minimum amplitude difference in consecutive samples to be considered as 'clipped' (default = 0)  
                                             string, percent of the amplitude range considered as 'clipped' (i.e. '1%')  
         
        The output argument "artifact" is a Nx2 matrix comparable to the "trl" matrix of  
        FT_DEFINETRIAL. The first column of which specifying the beginsamples of an  
        artifact period, the second column contains the endsamples of the artifactperiods.  
         
        To facilitate data-handling and distributed computing, you can use  
          cfg.inputfile   =  ...  
        to read the input data from a *.mat file on disk. This mat files should contain  
        only a single variable named 'data', corresponding to the input structure.  
         
        See also FT_REJECTARTIFACT, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG, FT_ARTIFACT_EOG,  
        FT_ARTIFACT_JUMP, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_ZVALUE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_artifact_clip.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_artifact_clip", *args, **kwargs)
