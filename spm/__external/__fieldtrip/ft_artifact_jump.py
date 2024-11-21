from spm.__wrapper__ import Runtime


def ft_artifact_jump(*args, **kwargs):
    """
      FT_ARTIFACT_JUMP scans data segments of interest for SQUID jump artifacts.  
         
        Use as  
          [cfg, artifact] = ft_artifact_jump(cfg)  
        with the configuration options  
          cfg.dataset    = string with the filename  
        or  
          cfg.headerfile = string with the filename  
          cfg.datafile   = string with the filename  
        and optionally  
          cfg.headerformat  
          cfg.dataformat  
         
        Alternatively you can use it as  
          [cfg, artifact] = ft_artifact_jump(cfg, data)  
        where the input data is a structure as obtained from FT_PREPROCESSING.  
         
        In both cases the configuration should also contain  
          cfg.trl        = structure that defines the data segments of interest, see FT_DEFINETRIAL  
          cfg.continuous = 'yes' or 'no' whether the file contains continuous data  
         
        Prior to artifact detection, the data is preprocessed (again) with the following  
        configuration parameters, which are optimal for identifying SQUID jump artifacts.  
          cfg.artfctdef.jump.medianfilter  = 'yes'  
          cfg.artfctdef.jump.medianfiltord = 9  
          cfg.artfctdef.jump.absdiff       = 'yes'  
         
        Artifacts are identified by means of thresholding the z-transformed value  
        of the preprocessed data.  
          cfg.artfctdef.jump.channel       = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details  
          cfg.artfctdef.jump.cutoff        = z-value at which to threshold (default = 20)  
          cfg.artfctdef.jump.trlpadding    = number in seconds (default = 0.0)  
          cfg.artfctdef.jump.fltpadding    = number in seconds (default = 0.0)  
          cfg.artfctdef.jump.artpadding    = number in seconds (default = 0.0)  
         
        The output argument "artifact" is a Nx2 matrix comparable to the "trl" matrix of  
        FT_DEFINETRIAL. The first column of which specifying the beginsamples of an  
        artifact period, the second column contains the endsamples of the artifactperiods.  
         
        To facilitate data-handling and distributed computing, you can use  
          cfg.inputfile   =  ...  
        to read the input data from a *.mat file on disk. This mat files should contain  
        only a single variable named 'data', corresponding to the input structure.  
         
        See also FT_REJECTARTIFACT, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG, FT_ARTIFACT_EOG,  
        FT_ARTIFACT_JUMP, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_ZVALUE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_artifact_jump.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_artifact_jump", *args, **kwargs)
