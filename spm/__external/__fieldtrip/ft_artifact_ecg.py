from spm.__wrapper__ import Runtime


def ft_artifact_ecg(*args, **kwargs):
    """
      FT_ARTIFACT_ECG performs a peak-detection on the ECG-channel and identifies the  
        windows around the QRS peak as artifacts. Using FT_REJECTARTIFACT you can remove  
        these windows from your data, or using FT_REMOVETEMPLATEARTIFACT you can subtract  
        an averaged template artifact from your data.  
         
        Use as  
          [cfg, artifact] = ft_artifact_ecg(cfg)  
        with the configuration options  
          cfg.dataset     = string with the filename  
        or  
          cfg.headerfile  = string with the filename  
          cfg.datafile    = string with the filename  
        and optionally  
          cfg.headerformat  
          cfg.dataformat  
         
        Alternatively you can use it as  
          [cfg, artifact] = ft_artifact_ecg(cfg, data)  
        where the input data is a structure as obtained from FT_PREPROCESSING.  
         
        In both cases the configuration should also contain  
          cfg.trl        = structure that defines the data segments of interest. See FT_DEFINETRIAL  
          cfg.continuous = 'yes' or 'no' whether the file contains continuous data  
        and  
          cfg.artfctdef.ecg.channel = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details  
          cfg.artfctdef.ecg.pretim  = pre-artifact rejection interval in seconds (default = 0.05)  
          cfg.artfctdef.ecg.psttim  = post-artifact rejection interval in seconds (default = 0.3)  
          cfg.artfctdef.ecg.cutoff  = peak threshold (default = 3)  
          cfg.artfctdef.ecg.inspect = Nx1 list of channels which will be shown as a QRS-locked average  
         
        The output argument "artifact" is a Nx2 matrix comparable to the "trl" matrix of  
        FT_DEFINETRIAL. The first column of which specifying the begin samples of an  
        artifact period, the second column contains the end samples of the QRS periods.  
         
        To facilitate data-handling and distributed computing, you can use  
          cfg.inputfile   =  ...  
        to read the input data from a *.mat file on disk. This mat files should contain  
        only a single variable named 'data', corresponding to the input structure.  
         
        See also FT_REJECTARTIFACT, FT_REMOVETEMPLATEARTIFACT, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG,  
        FT_ARTIFACT_EOG, FT_ARTIFACT_JUMP, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_THRESHOLD,  
        FT_ARTIFACT_ZVALUE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_artifact_ecg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_artifact_ecg", *args, **kwargs)
