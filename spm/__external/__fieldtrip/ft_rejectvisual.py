from spm.__wrapper__ import Runtime


def ft_rejectvisual(*args, **kwargs):
    """
      FT_REJECTVISUAL shows the preprocessed data in all channels and/or trials to allow  
        the user to make a visual selection of the data that should be rejected. The data  
        can be displayed in a "summary" mode, in which case the variance (or another  
        metric) in each channel and each trial is computed. Alternatively, all channels can  
        be shown at once allowing paging through the trials, or all trials can be shown,  
        allowing paging through the channels.  
         
        Use as  
          [data] = ft_rejectvisual(cfg, data)  
         
        The configuration can contain  
          cfg.method      = string, describes how the data should be shown, this can be  
                            'summary'  show a single number for each channel and trial (default)  
                            'channel'  show the data per channel, all trials at once  
                            'trial'    show the data per trial, all channels at once  
          cfg.channel     = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details  
          cfg.keepchannel = string, determines how to deal with channels that are not selected, can be  
                            'no'          completely remove deselected channels from the data (default)  
                            'yes'         keep deselected channels in the output data  
                            'nan'         fill the channels that are deselected with NaNs  
                            'zero'        fill the channels that are deselected with zeros  
                            'repair'      repair the deselected channels using FT_CHANNELREPAIR  
          cfg.trials      = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.keeptrial   = string, determines how to deal with trials that are  
                            not selected, can be  
                            'no'     completely remove deselected trials from the data (default)  
                            'yes'    keep deselected trials in the output data  
                            'nan'    fill the trials that are deselected with NaNs  
                            'zero'   fill the trials that are deselected with zeros  
          cfg.metric      = string, describes the metric that should be computed in summary mode  
                            for each channel in each trial, can be  
                            'var'          variance within each channel (default)  
                            'std'          standard deviation within each channel  
                            'db'           decibel value within each channel  
                            'mad'          median absolute deviation within each channel  
                            '1/var'        inverse variance within each channel  
                            'min'          minimum value in each channel  
                            'max'          maximum value each channel  
                            'maxabs'       maximum absolute value in each channel  
                            'range'        range from min to max in each channel  
                            'kurtosis'     kurtosis, i.e. measure of peakedness of the amplitude distribution  
                            'zvalue'       mean and std computed over all time and trials, per channel  
                            'neighbexpvar' relative variance explained by neighboring channels in each trial  
          cfg.neighbours  = neighbourhood structure, see FT_PREPARE_NEIGHBOURS for details  
          cfg.latency     = [begin end] in seconds, or 'all', 'minperiod', 'maxperiod', 'prestim', 'poststim' (default = 'all')  
          cfg.viewmode    = 'remove', 'toggle' or 'hide', only applies to summary mode (default = 'remove')  
          cfg.box         = string, 'yes' or 'no' whether to draw a box around each graph (default = 'no')  
          cfg.ylim        = 'maxmin', 'maxabs', 'zeromax', 'minzero', or [ymin ymax] (default = 'maxmin')  
         
        The following options for the scaling of the EEG, EOG, ECG, EMG, MEG and NIRS channels  
        is optional and can be used to bring the absolute numbers of the different  
        channel types in the same range (e.g. fT and uV). The channel types are determined  
        from the input data using FT_CHANNELSELECTION.  
          cfg.eegscale    = number, scaling to apply to the EEG channels prior to display  
          cfg.eogscale    = number, scaling to apply to the EOG channels prior to display  
          cfg.ecgscale    = number, scaling to apply to the ECG channels prior to display  
          cfg.emgscale    = number, scaling to apply to the EMG channels prior to display  
          cfg.megscale    = number, scaling to apply to the MEG channels prior to display  
          cfg.gradscale   = number, scaling to apply to the MEG gradiometer channels prior to display (in addition to the cfg.megscale factor)  
          cfg.magscale    = number, scaling to apply to the MEG magnetometer channels prior to display (in addition to the cfg.megscale factor)  
          cfg.nirsscale   = number, scaling to apply to the NIRS channels prior to display  
          cfg.mychanscale = number, scaling to apply to the channels specified in cfg.mychan  
          cfg.mychan      = Nx1 cell-array with selection of channels  
          cfg.chanscale   = Nx1 vector with scaling factors, one per channel specified in cfg.channel  
         
        Optionally, the raw data is preprocessed (filtering etc.) prior to displaying it or  
        prior to computing the summary metric. The preprocessing and the selection of the  
        latency window is NOT applied to the output data.  
         
        The following settings are useful for identifying EOG artifacts:  
          cfg.preproc.bpfilter    = 'yes'  
          cfg.preproc.bpfilttype  = 'but'  
          cfg.preproc.bpfreq      = [1 15]  
          cfg.preproc.bpfiltord   = 4  
          cfg.preproc.rectify     = 'yes'  
         
        The following settings are useful for identifying muscle artifacts:  
          cfg.preproc.bpfilter    = 'yes'  
          cfg.preproc.bpfreq      = [110 140]  
          cfg.preproc.bpfiltord   =  8  
          cfg.preproc.bpfilttype  = 'but'  
          cfg.preproc.rectify     = 'yes'  
          cfg.preproc.boxcar      = 0.2  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_REJECTARTIFACT, FT_REJECTCOMPONENT, FT_BADSEGMENT, FT_BADCHANNEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_rejectvisual.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_rejectvisual", *args, **kwargs)
