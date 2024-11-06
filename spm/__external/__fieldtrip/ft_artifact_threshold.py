from spm.__wrapper__ import Runtime


def ft_artifact_threshold(*args, **kwargs):
    """
      FT_ARTIFACT_THRESHOLD scans data segments of interest for channels in which the  
        signal exceeds a specified minimum or maximum value, or in which the peak-to-peak  
        range within the trial exceeds a specified threshold.  
         
        Use as  
          [cfg, artifact] = ft_artifact_threshold(cfg)  
        with the configuration options  
          cfg.dataset     = string with the filename  
        or  
          cfg.headerfile  = string with the filename  
          cfg.datafile    = string with the filename  
        and optionally  
          cfg.headerformat  
          cfg.dataformat  
         
        Alternatively you can use it as  
          [cfg, artifact] = ft_artifact_threshold(cfg, data)  
        where the input data is a structure as obtained from FT_PREPROCESSING.  
         
        In both cases the configuration should also contain  
          cfg.trl        = structure that defines the data segments of interest, see FT_DEFINETRIAL  
          cfg.continuous = 'yes' or 'no' whether the file contains continuous data  
        and  
          cfg.artfctdef.threshold.channel   = cell-array with channel labels  
          cfg.artfctdef.threshold.bpfilter  = 'no' or 'yes' (default = 'yes')  
          cfg.artfctdef.threshold.bpfreq    = [0.3 30]  
          cfg.artfctdef.threshold.bpfiltord = 4  
         
        In the same way as specifying the options for band-pass filtering, it is also  
        possible to specify lpfilter, hpfilter, bsfilter, dftfilter or medianfilter, see  
        FT_PREPROCESSING.  
         
        The detection of artifacts is done according to the following settings,  
        you should specify at least one of these thresholds  
          cfg.artfctdef.threshold.min       = value in uV or T, default -inf  
          cfg.artfctdef.threshold.max       = value in uV or T, default  inf  
          cfg.artfctdef.threshold.onset     = value in uV or T, default  inf  
          cfg.artfctdef.threshold.offset    = value in uV or T, default  inf  
         
        When cfg.artfctdef.threshold.onset and offset are used, the rising and falling  
        flank are thresholded with different values. In case onset and offset are both  
        positive, the data will be thresholded above their values. In case both onset and  
        offset are negative, the data will be thresholded below their values.  
         
        Note that this function does not support artifactpadding or filterpadding.  
         
        The output argument "artifact" is a Nx2 matrix comparable to the "trl" matrix of  
        FT_DEFINETRIAL. The first column of which specifying the beginsamples of an  
        artifact period, the second column contains the endsamples of the artifactperiods.  
         
        To facilitate data-handling and distributed computing, you can use  
          cfg.inputfile   =  ...  
        to read the input data from a *.mat file on disk. This mat files should contain  
        only a single variable named 'data', corresponding to the input structure.  
         
        See also FT_REJECTARTIFACT, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG, FT_ARTIFACT_EOG,  
        FT_ARTIFACT_JUMP, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_ZVALUE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_artifact_threshold.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_artifact_threshold", *args, **kwargs)
