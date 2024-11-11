from spm.__wrapper__ import Runtime


def ft_artifact_tms(*args, **kwargs):
    """
      FT_ARTIFACT_TMS reads the data segments of interest from file and identifies  
        artefacts in EEG recordings that were done during TMS stimulation.  
         
        Use as  
          [cfg, artifact] = ft_artifact_tms(cfg)  
        with the configuration options  
          cfg.dataset     = string with the filename  
        or  
          cfg.headerfile  = string with the filename  
          cfg.datafile    = string with the filename  
        and optionally  
          cfg.headerformat  
          cfg.dataformat  
         
        Alternatively you can use it as  
          [cfg, artifact] = ft_artifact_tms(cfg, data)  
        where the input data is a structure as obtained from FT_PREPROCESSING.  
         
        In both cases the configuration should also contain  
          cfg.trl         = structure that defines the data segments of interest, see FT_DEFINETRIAL  
          cfg.continuous  = 'yes' or 'no' whether the file contains continuous data (default = 'yes')  
        and  
          cfg.method      = 'detect' or 'marker', see below.  
          cfg.prestim     = scalar, time in seconds prior to onset of detected event to mark as artifactual (default = 0.005 seconds)  
          cfg.poststim    = scalar, time in seconds post onset of detected even to mark as artifactual (default = 0.010 seconds)  
         
        The different methods are described in detail below.  
         
        With cfg.method='detect', TMS-artifact are detected on basis of transient  
        high-amplidude gradients that are typical for TMS-pulses. The data is preprocessed  
        (again) with the following settings, which are optimal for identifying TMS-pulses.  
        Artifacts are identified by means of thresholding the z-transformed value of the  
        preprocessed data. This method acts as a wrapper around FT_ARTIFACT_ZVALUE.  
          cfg.artfctdef.tms.derivative  = 'yes'  
          cfg.artfctdef.tms.channel     = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details  
          cfg.artfctdef.tms.cutoff      = z-value at which to threshold (default = 4)  
          cfg.artfctdef.tms.trlpadding  = 0.1  
          cfg.artfctdef.tms.fltpadding  = 0.1  
          cfg.artfctdef.tms.artpadding  = 0.01  
        Be aware that if one artifact falls within this specified range of another  
        artifact, both artifact will be counted as one. Depending on cfg.prestim and  
        cfg.poststim you may not mark enough data as artifactual.  
         
        With cfg.method='marker', TMS-artifact onsets and offsets are based on  
        markers/triggers that are written into the EEG dataset. This method acts as a  
        wrapper around FT_DEFINETRIAL to determine on- and offsets of TMS pulses by reading  
        markers in the EEG.  
          cfg.trialfun            = function name, see below (default = 'ft_trialfun_general')  
          cfg.trialdef.eventtype  = 'string'  
          cfg.trialdef.eventvalue = number, string or list with numbers or strings  
        The cfg.trialfun option is a string containing the name of a function that you  
        wrote yourself and that FT_ARTIFACT_TMS will call. The function should take the  
        cfg-structure as input and should give a NxM matrix with M>=3 in the same format as  
        "trl" as the output. You can add extra custom fields to the configuration structure  
        to pass as arguments to your own trialfun. Furthermore, inside the trialfun you can  
        use the FT_READ_EVENT function to get the event information from your data file.  
         
        The output argument "artifact" is a Nx2 matrix comparable to the "trl" matrix of  
        FT_DEFINETRIAL. The first column of which specifying the beginsamples of an  
        artifact period, the second column contains the endsamples of the artifactperiods.  
         
        To facilitate data-handling and distributed computing, you can use  
          cfg.inputfile   =  ...  
        to read the input data from a *.mat file on disk. This mat files should contain  
        only a single variable named 'data', corresponding to the input structure.  
         
        See also FT_REJECTARTIFACT, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG, FT_ARTIFACT_EOG,  
        FT_ARTIFACT_JUMP, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_ZVALUE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_artifact_tms.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_artifact_tms", *args, **kwargs)
