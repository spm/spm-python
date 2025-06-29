from spm._runtime import Runtime


def ft_definetrial(*args, **kwargs):
    """
      FT_DEFINETRIAL defines the trials or segments of data that will be used for further  
        processing and analysis, i.e. the pieces of data that will be read in by  
        FT_PREPROCESSING. Trials are defined by their begin and end sample in the data file  
        and each trial has an offset that defines where the relative t=0 point (usually the  
        sample at which the trigger is detected) is for that trial or segment.  
         
        Use as  
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.trialdef       = structure with the details of trial definition, see below  
          cfg.trialfun       = string with the function name, see below (default = 'ft_trialfun_general')  
          cfg.representation = 'numeric' or 'table', determines how the trial definition is returned (default is automatic)  
        and furthermore  
          cfg.dataset        = string with the filename  
        or  
          cfg.headerfile     = string with the filename  
          cfg.datafile       = string with the filename  
        and optionally  
          cfg.headerformat   = string, see FT_FILETYPE (default is automatic)  
          cfg.dataformat     = string, see FT_FILETYPE (default is automatic)  
          cfg.eventformat    = string, see FT_FILETYPE (default is automatic)  
         
        In general, a call to FT_DEFINETRIAL results in the trial definition "trl" being  
        added to the output configuration. The trials are defined on the basis of events or  
        triggers by a user-specified MATLAB function that is subsequently referred to as  
        the trial function. The user can specify their own custom function tailored to the  
        experimental paradigm, or use one of the default trial functions (see below).  
         
        Simple trial definitions (for example based on a single trigger) are supported by  
        FT_TRIALFUN_GENERAL, which is specified as the default. It supports the following  
        options  
          cfg.trialdef.eventtype  = string, or cell-array with strings  
          cfg.trialdef.eventvalue = number, string, or list with numbers or strings  
          cfg.trialdef.prestim    = number, latency in seconds (optional)  
          cfg.trialdef.poststim   = number, latency in seconds (optional)  
         
        To read all data from a continuous file in a single or in multiple segments,  
        FT_TRIALFUN_GENERAL understands the following options  
           cfg.trialdef.triallength = duration in seconds (can also be 1 or Inf)  
           cfg.trialdef.ntrials     = number of trials (can also be 1 or Inf)  
           cfg.trialdef.overlap     = number between 0 and 1 (exclusive) specifying the fraction of overlap between snippets (0 = no overlap)  
         
        To display a list with the events in your data on screen, you can use  
        FT_TRIALFUN_SHOW. This is useful for diagnostics; no actual trials will be defined.  
         
        To display a graphical user interface dialog that allows you to select events of  
        interest, you can use FT_TRIALFUN_GUI.  
         
        The trial definition "trl" is an Nx3 matrix or table, where N is the number of  
        trials. The first column contains the sample-indices of the start of each trial  
        relative to the start of the raw data, the second column contains the sample  
        indices of the end of each trial, and the third column contains the offset of the  
        trigger with respect to the trial. An offset of 0 means that the first sample of  
        the trial corresponds to the trigger. A positive offset indicates that the first  
        sample is later than the trigger, and a negative offset indicates that the trial  
        begins before the trigger.  
         
        Besides the required three columns in the trial definition "trl" that represent  
        start, end and offset, it can have contain additional columns . These additional  
        columns can be used by a custom trialfun to provide  information about each trial,  
        such as trigger codes, response latencies, trial type, and response correctness.  
        After FT_PREPROCESSING these additional columns of the "trl" matrix will be  
        represented in the "trialinfo" field.  
         
        If FT_TRIALFUN_GENERAL or FT_TRIALFUN_GUI has been used to generate the "trl"  
        matrix or table, the function may return a fourth column that refers to the  
        event-code for the corresponding trial. Whether or not this column is returned  
        depends on the acquisition system. In general, this fourth column is generated by  
        default if the event codes are represented numerically, or as a string starting  
        with 'S' or 'R' (for BrainVision data).  
         
        If you need to define the segments of interest on the basis of a conditional  
        sequence of events (e.g. stimulus trigger followed by a correct response) or on  
        basis of some signal feature that needs to be detected in the data, you should  
        supply in cfg.trialfun the name of a function that you wrote yourself and that  
        FT_DEFINETRIAL will call. The function receives the cfg structure as input and  
        should return a NxM matrix in the same format as "trl" as the output. You can add  
        extra custom fields to cfg.trialdef to pass to your own trialfun. See below for  
        pointers to some examples.  
         
        See also FT_PREPROCESSING, FT_READ_HEADER, FT_READ_EVENT, FT_TRIALFUN_GENERAL,  
        FT_TRIALFUN_GUI, FT_TRIALFUN_SHOW, FT_TRIALFUN_BIDS, FT_TRIALFUN_EXAMPLE1,  
        FT_TRIALFUN_EXAMPLE2  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_definetrial.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_definetrial", *args, **kwargs)
