from spm.__wrapper__ import Runtime


def ft_preprocessing(*args, **kwargs):
    """
      FT_PREPROCESSING reads MEG and/or EEG data according to user-specified trials  
        and applies several user-specified preprocessing steps to the signals.  
         
        Use as  
          [data] = ft_preprocessing(cfg)  
        or  
          [data] = ft_preprocessing(cfg, data)  
         
        The first input argument "cfg" is the configuration structure, which contains all  
        details for the dataset filename, trials and the preprocessing options.  
         
        If you are calling FT_PREPROCESSING with only the configuration as first input  
        argument and the data still has to be read from file, you should specify  
          cfg.dataset      = string with the filename  
          cfg.trl          = Nx3 matrix with the trial definition, see FT_DEFINETRIAL  
          cfg.padding      = length (in seconds) to which the trials are padded for filtering (default = 0)  
          cfg.padtype      = string, type of padding (default: 'data' padding or  
                             'mirror', depending on feasibility)  
          cfg.continuous   = 'yes' or 'no' whether the file contains continuous data  
                             (default is determined automatic)  
         
        Instead of specifying the dataset in the configuration, you can also explicitly  
        specify the name of the file containing the header information and the name of the  
        file containing the data, using  
          cfg.datafile     = string with the filename  
          cfg.headerfile   = string with the filename  
         
        If you are calling FT_PREPROCESSING with the second input argument "data", then  
        that should contain data that was already read from file in a previous call to  
        FT_PREPROCESSING. In that case only the configuration options below apply.  
         
        The channels that will be read and/or preprocessed are specified with  
          cfg.channel      = Nx1 cell-array with selection of channels (default = 'all'),  
                             see FT_CHANNELSELECTION for details  
          cfg.chantype     = string or Nx1 cell-array with channel types to be read (only for NeuroOmega)  
         
        The preprocessing options for the selected channels are specified with  
          cfg.lpfilter      = 'no' or 'yes'  lowpass filter (default = 'no')  
          cfg.hpfilter      = 'no' or 'yes'  highpass filter (default = 'no')  
          cfg.bpfilter      = 'no' or 'yes'  bandpass filter (default = 'no')  
          cfg.bsfilter      = 'no' or 'yes'  bandstop filter (default = 'no')  
          cfg.dftfilter     = 'no' or 'yes'  line noise removal using discrete fourier transform (default = 'no')  
          cfg.medianfilter  = 'no' or 'yes'  jump preserving median filter (default = 'no')  
          cfg.lpfreq        = lowpass  frequency in Hz  
          cfg.hpfreq        = highpass frequency in Hz  
          cfg.bpfreq        = bandpass frequency range, specified as [lowFreq highFreq] in Hz  
          cfg.bsfreq        = bandstop frequency range, specified as [low high] in Hz (or as Nx2 matrix for notch filter)  
          cfg.dftfreq       = line noise frequencies in Hz for DFT filter (default = [50 100 150])  
          cfg.lpfiltord     = lowpass  filter order (default set in low-level function)  
          cfg.hpfiltord     = highpass filter order (default set in low-level function)  
          cfg.bpfiltord     = bandpass filter order (default set in low-level function)  
          cfg.bsfiltord     = bandstop filter order (default set in low-level function)  
          cfg.lpfilttype    = digital filter type, 'but' or 'firws' or 'fir' or 'firls' (default = 'but')  
          cfg.hpfilttype    = digital filter type, 'but' or 'firws' or 'fir' or 'firls' (default = 'but')  
          cfg.bpfilttype    = digital filter type, 'but' or 'firws' or 'fir' or 'firls' (default = 'but')  
          cfg.bsfilttype    = digital filter type, 'but' or 'firws' or 'fir' or 'firls' (default = 'but')  
          cfg.lpfiltdir     = filter direction, 'twopass' (default), 'onepass' or 'onepass-reverse' or 'onepass-zerophase' (default for firws) or 'onepass-minphase' (firws, non-linear!)  
          cfg.hpfiltdir     = filter direction, 'twopass' (default), 'onepass' or 'onepass-reverse' or 'onepass-zerophase' (default for firws) or 'onepass-minphase' (firws, non-linear!)  
          cfg.bpfiltdir     = filter direction, 'twopass' (default), 'onepass' or 'onepass-reverse' or 'onepass-zerophase' (default for firws) or 'onepass-minphase' (firws, non-linear!)  
          cfg.bsfiltdir     = filter direction, 'twopass' (default), 'onepass' or 'onepass-reverse' or 'onepass-zerophase' (default for firws) or 'onepass-minphase' (firws, non-linear!)  
          cfg.lpinstabilityfix = deal with filter instability, 'no', 'reduce', 'split' (default  = 'no')  
          cfg.hpinstabilityfix = deal with filter instability, 'no', 'reduce', 'split' (default  = 'no')  
          cfg.bpinstabilityfix = deal with filter instability, 'no', 'reduce', 'split' (default  = 'no')  
          cfg.bsinstabilityfix = deal with filter instability, 'no', 'reduce', 'split' (default  = 'no')  
          cfg.lpfiltdf      = lowpass transition width (firws, overrides order, default set in low-level function)  
          cfg.hpfiltdf      = highpass transition width (firws, overrides order, default set in low-level function)  
          cfg.bpfiltdf      = bandpass transition width (firws, overrides order, default set in low-level function)  
          cfg.bsfiltdf      = bandstop transition width (firws, overrides order, default set in low-level function)  
          cfg.lpfiltwintype = lowpass window type, 'hann' or 'hamming' (default) or 'blackman' or 'kaiser' (firws)  
          cfg.hpfiltwintype = highpass window type, 'hann' or 'hamming' (default) or 'blackman' or 'kaiser' (firws)  
          cfg.bpfiltwintype = bandpass window type, 'hann' or 'hamming' (default) or 'blackman' or 'kaiser' (firws)  
          cfg.bsfiltwintype = bandstop window type, 'hann' or 'hamming' (default) or 'blackman' or 'kaiser' (firws)  
          cfg.lpfiltdev     = lowpass max passband deviation (firws with 'kaiser' window, default 0.001 set in low-level function)  
          cfg.hpfiltdev     = highpass max passband deviation (firws with 'kaiser' window, default 0.001 set in low-level function)  
          cfg.bpfiltdev     = bandpass max passband deviation (firws with 'kaiser' window, default 0.001 set in low-level function)  
          cfg.bsfiltdev     = bandstop max passband deviation (firws with 'kaiser' window, default 0.001 set in low-level function)  
          cfg.dftreplace    = 'zero' or 'neighbour', method used to reduce line noise, 'zero' implies DFT filter, 'neighbour' implies spectrum interpolation (default = 'zero')  
          cfg.dftbandwidth  = bandwidth of line noise frequencies, applies to spectrum interpolation, in Hz (default = [1 2 3])  
          cfg.dftneighbourwidth = bandwidth of frequencies neighbouring line noise frequencies, applies to spectrum interpolation, in Hz (default = [2 2 2])  
          cfg.plotfiltresp  = 'no' or 'yes', plot filter responses (firws, default = 'no')  
          cfg.usefftfilt    = 'no' or 'yes', use fftfilt instead of filter (firws, default = 'no')  
          cfg.medianfiltord = length of median filter (default = 9)  
          cfg.demean        = 'no' or 'yes', whether to apply baseline correction (default = 'no')  
          cfg.baselinewindow = [begin end] in seconds, the default is the complete trial (default = 'all')  
          cfg.detrend       = 'no' or 'yes', remove linear trend from the data (done per trial) (default = 'no')  
          cfg.polyremoval   = 'no' or 'yes', remove higher order trend from the data (done per trial) (default = 'no')  
          cfg.polyorder     = polynome order for poly trend removal (default = 2; note that all lower-order trends will also be removed when using cfg.polyremoval)  
          cfg.derivative    = 'no' or 'yes', computes the first order derivative of the data (default = 'no')  
          cfg.hilbert       = 'no', 'abs', 'complex', 'real', 'imag', 'absreal', 'absimag' or 'angle' (default = 'no')  
          cfg.rectify       = 'no' or 'yes' (default = 'no')  
          cfg.precision     = 'single' or 'double' (default = 'double')  
          cfg.absdiff       = 'no' or 'yes', computes absolute derivative (i.e. first derivative then rectify)  
         
        Preprocessing options that only apply to MEG data are  
          cfg.coordsys      = string, 'head' or 'dewar' (default = 'head')  
          cfg.coilaccuracy  = can be empty or a number (0, 1 or 2) to specify the accuracy (default = [])  
          cfg.coildeffile   = can be empty or a string to a custom coil_def.dat file (default = [])  
         
        Preprocessing options that you should only use for EEG data are  
          cfg.reref         = 'no' or 'yes' (default = 'no')  
          cfg.refchannel    = cell-array with new EEG reference channel(s), this can be 'all' for a common average reference  
          cfg.refmethod     = 'avg', 'median', 'rest', 'bipolar' or 'laplace' (default = 'avg')  
          cfg.groupchans    = 'yes' or 'no', should channels be rereferenced in separate groups for bipolar and laplace methods,  
                              this requires channnels to be named using an alphanumeric code, where letters represent the group  
                              and numbers represent the order of the channel whithin its group (default = 'no')  
          cfg.leadfield     = leadfield structure, this is required when cfg.refmethod='rest', see FT_PREPARE_LEADFIELD  
          cfg.implicitref   = 'label' or empty, add the implicit EEG reference as zeros (default = [])  
          cfg.montage       = 'no' or a montage structure, see FT_APPLY_MONTAGE (default = 'no')  
         
        Preprocessing options that you should only use when you are calling FT_PREPROCESSING with  
        also the second input argument "data" are  
          cfg.trials        = 'all' or a selection given as a 1xN vector (default = 'all')  
         
        Preprocessing options that you should only use when you are calling  
        FT_PREPROCESSING with a single cfg input argument are  
          cfg.method        = 'trial' or 'channel', read data per trial or per channel (default = 'trial')  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_DEFINETRIAL, FT_REDEFINETRIAL, FT_APPENDDATA, FT_APPENDSPIKE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_preprocessing.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preprocessing", *args, **kwargs)
