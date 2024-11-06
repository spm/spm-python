from spm.__wrapper__ import Runtime


def ft_rejectartifact(*args, **kwargs):
    """
      FT_REJECTARTIFACT removes data segments containing artifacts. It returns a  
        configuration structure with a modified trial definition which can be used for  
        preprocessing of only the clean data.  
         
        You should start by detecting the artifacts in the data using the function  
        FT_ARTIFACT_xxx where xxx is the type of artifact. Subsequently FT_REJECTARTIFACT  
        looks at the detected artifacts and removes them from the trial definition or from  
        the data. In case you wish to replace bad parts by NaNs, you have to specify data  
        as an input parameter.  
         
        Use as  
          [cfg] = ft_rejectartifact(cfg)  
        with the cfg as obtained from FT_DEFINETRIAL, or as  
          [data] = ft_rejectartifact(cfg, data)  
        with the data as obtained from FT_PREPROCESSING  
         
        The following configuration options are supported  
          cfg.artfctdef.reject          = 'none', 'partial', 'complete', 'nan', 'zero', or 'value' (default = 'complete')  
          cfg.artfctdef.minaccepttim    = when using partial rejection, minimum length  
                                          in seconds of remaining trial (default = 0.1)  
          cfg.artfctdef.crittoilim      = when using complete rejection, reject trial only when artifacts occur within  
                                          this time window (default = whole trial). This only works with in-memory data,  
                                          since trial time axes are unknown for data on disk.  
          cfg.artfctdef.feedback        = 'yes' or 'no' (default = 'no')  
          cfg.artfctdef.invert          = 'yes' or 'no' (default = 'no')  
          cfg.artfctdef.value           = scalar value to replace the data in the artifact segments (default = nan)  
          cfg.artfctdef.eog.artifact    = Nx2 matrix with artifact segments, this is added to the cfg by using FT_ARTIFACT_EOG  
          cfg.artfctdef.jump.artifact   = Nx2 matrix with artifact segments, this is added to the cfg by using FT_ARTIFACT_JUMP  
          cfg.artfctdef.muscle.artifact = Nx2 matrix with artifact segments, this is added to the cfg by using FT_ARTIFACT_MUSCLE  
          cfg.artfctdef.zvalue.artifact = Nx2 matrix with artifact segments, this is added to the cfg by using FT_ARTIFACT_ZVALUE  
          cfg.artfctdef.visual.artifact = Nx2 matrix with artifact segments, this is added to the cfg by using FT_DATABROWSER  
          cfg.artfctdef.xxx.artifact    = Nx2 matrix with artifact segments, this could be added by your own artifact detection function  
         
        A trial that contains an artifact can be rejected completely or partially. In case  
        of partial rejection, a minimum length of the resulting sub-trials can be specified  
        using minaccepttim.  
         
        Output:  
          If cfg is the only input parameter, the output is a cfg structure with an updated trl.  
          If cfg and data are both input parameters, the output is an updated raw data structure with only the clean data segments.  
          If cfg and data are both input parameters, and the cfg contains a trl field, an error is thrown.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
        If you specify this option the input data will be read from a *.mat  
        file on disk. This mat files should contain only a single variable named 'data',  
        corresponding to the input structure.  
         
        See also FT_ARTIFACT_ZVALUE, FT_ARTIFACT_EOG, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_JUMP,  
        FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG, FT_DATABROWSER,  
        FT_REJECTVISUAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_rejectartifact.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_rejectartifact", *args, **kwargs)
