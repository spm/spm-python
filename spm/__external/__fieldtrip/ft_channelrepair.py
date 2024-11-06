from spm.__wrapper__ import Runtime


def ft_channelrepair(*args, **kwargs):
    """
      FT_CHANNELREPAIR repairs bad or missing channels in the data by replacing  
        them with the plain average of of all neighbours, by a weighted average  
        of all neighbours, by an interpolation based on a surface Laplacian, or  
        by spherical spline interpolating (see Perrin et al., 1989).  
         
        Use as  
          [interp] = ft_channelrepair(cfg, data)  
        where the input data corresponds to the output from FT_PREPROCESSING.  
         
        The configuration should contain  
          cfg.method         = 'weighted', 'average', 'spline', 'slap' or 'nan' (default = 'weighted')  
          cfg.badchannel     = cell-array, see FT_CHANNELSELECTION for details  
          cfg.missingchannel = cell-array, see FT_CHANNELSELECTION for details  
          cfg.neighbours     = neighbourhood structure, see FT_PREPARE_NEIGHBOURS for details  
          cfg.trials         = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.lambda         = regularisation parameter (default = 1e-5, for method 'spline' and 'slap')  
          cfg.order          = order of the polynomial interpolation (default = 4 for methods 'spline' and 'slap')  
          cfg.senstype       = string, which type of data to repair. Can be 'meg', 'eeg' or 'nirs' (default is automatic)  
         
        The weighted and average method are less reliable in case multiple bad channels lie  
        next to each other. In that case the bad channels will be removed from the  
        neighbours and not considered for interpolation.  
         
        If you want to reconstruct channels that are absent in your data, those  
        channels may also be missing from the sensor definition (grad, elec or opto)  
        and determining the neighbours is non-trivial. In that case you must use  
        a complete sensor definition from another dataset or from a template.  
         
        The EEG, MEG or NIRS sensor positions can be present as a field in the  
        data (data.grad/data.elec/data.opto, depending on the type of data),  
        or can be specified as cfg option. Either one is required for the following  
        methods: 'weighted', 'spline', and 'slap'. Depending on the type of  
        data this should be one of the following  
          cfg.elec = structure with electrode positions or filename, see FT_READ_SENS  
          cfg.grad = structure with gradiometer definition or filename, see FT_READ_SENS  
          cfg.opto = structure with optode definition, see FT_READ_SENS  
         
        This function will only repair one type of channels (MEG, EEG or NIRS) at  
        a time. If you want to repair multiple types of channels, you should call  
        it multiple times and use FT_SELECTDATA and FT_APPENDDATA.  
         
        This function only interpolates data over space, not over time. If you want to  
        interpolate using temporal information, e.g. using a segment of data before and  
        after the nan-marked artifact, you should use FT_INTERPOLATENAN.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_MEGREALIGN, FT_MEGPLANAR, FT_PREPARE_NEIGHBOURS, FT_INTERPOLATENAN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_channelrepair.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_channelrepair", *args, **kwargs)
