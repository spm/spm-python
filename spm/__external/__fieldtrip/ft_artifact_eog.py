from spm.__wrapper__ import Runtime


def ft_artifact_eog(*args, **kwargs):
    """
      FT_ARTIFACT_EOG scans data segments of interest for EOG artifacts.  
         
        Use as  
          [cfg, artifact] = ft_artifact_eog(cfg)  
        with the configuration options  
          cfg.dataset    = string with the filename  
        or  
          cfg.headerfile = string with the filename  
          cfg.datafile   = string with the filename  
        and optionally  
          cfg.headerformat  
          cfg.dataformat  
         
        Alternatively you can use it as  
          [cfg, artifact] = ft_artifact_eog(cfg, data)  
        where the input data is a structure as obtained from FT_PREPROCESSING.  
         
        In both cases the configuration should also contain  
          cfg.trl        = structure that defines the data segments of interest, see FT_DEFINETRIAL  
          cfg.continuous = 'yes' or 'no' whether the file contains continuous data  
         
        Prior to artifact detection, the data is preprocessed (again) with the following  
        configuration parameters, which are optimal for identifying EOG artifacts.  
          cfg.artfctdef.eog.bpfilter   = 'yes'  
          cfg.artfctdef.eog.bpfilttype = 'but'  
          cfg.artfctdef.eog.bpfreq     = [1 15]  
          cfg.artfctdef.eog.bpfiltord  = 4  
          cfg.artfctdef.eog.hilbert    = 'yes'  
         
        Artifacts are identified by means of thresholding the z-transformed value  
        of the preprocessed data.  
          cfg.artfctdef.eog.channel      = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details  
          cfg.artfctdef.eog.cutoff       = z-value at which to threshold (default = 4)  
          cfg.artfctdef.eog.trlpadding   = number in seconds (default = 0.5)  
          cfg.artfctdef.eog.fltpadding   = number in seconds (default = 0.1)  
          cfg.artfctdef.eog.artpadding   = number in seconds (default = 0.1)  
         
        The output argument "artifact" is a Nx2 matrix comparable to the "trl" matrix of  
        FT_DEFINETRIAL. The first column of which specifying the beginsamples of an  
        artifact period, the second column contains the endsamples of the artifactperiods.  
         
        To facilitate data-handling and distributed computing, you can use  
          cfg.inputfile   =  ...  
        to read the input data from a *.mat file on disk. This mat files should contain  
        only a single variable named 'data', corresponding to the input structure.  
         
        See also FT_REJECTARTIFACT, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG, FT_ARTIFACT_EOG,  
        FT_ARTIFACT_JUMP, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_ZVALUE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_artifact_eog.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_artifact_eog", *args, **kwargs)
