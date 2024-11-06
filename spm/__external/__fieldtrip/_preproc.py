from spm.__wrapper__ import Runtime


def _preproc(*args, **kwargs):
    """
      PREPROC applies various preprocessing steps on a single piece of EEG/MEG data  
        that has been read from a data file.  
         
        This low-level function serves as a subfunction for all FieldTrip modules that want  
        to preprocess the data, such as FT_PREPROCESSING, FT_ARTIFACT_XXX,  
        FT_TIMELOCKANALYSIS, etc. It ensures consistent handling of both MEG and EEG data  
        and consistency in the use of all preprocessing configuration options.  
         
        Use as  
          [dat, label, time, cfg] = preproc(dat, label, time, cfg, begpadding, endpadding)  
         
        The required input arguments are  
          dat         Nchan x Ntime data matrix  
          label       Nchan x 1 cell-array with channel labels  
          time        Ntime x 1 vector with the latency in seconds  
          cfg         configuration structure, see below  
        and the optional input arguments are  
          begpadding  number of samples that was used for padding (see below)  
          endpadding  number of samples that was used for padding (see below)  
         
        The output is  
          dat         Nchan x Ntime data matrix  
          label       Nchan x 1 cell-array with channel labels  
          time        Ntime x 1 vector with the latency in seconds  
          cfg         configuration structure, optionally with extra defaults set  
         
        Note that the number of input channels and the number of output channels can be  
        different, for example when the user specifies that he/she wants to add the  
        implicit EEG reference channel to the data matrix.  
         
        The filtering of the data can introduce artifacts at the edges, hence it is better  
        to pad the data with some extra signal at the begin and end. After filtering, this  
        padding is removed and the other preprocessing steps are applied to the remainder  
        of the data. The input fields begpadding and endpadding should be specified in  
        samples. You can also leave them empty, which implies that the data is not padded.  
         
        The configuration can contain  
          cfg.lpfilter      = 'no' or 'yes'  lowpass filter  
          cfg.hpfilter      = 'no' or 'yes'  highpass filter  
          cfg.bpfilter      = 'no' or 'yes'  bandpass filter  
          cfg.bsfilter      = 'no' or 'yes'  bandstop filter  
          cfg.dftfilter     = 'no' or 'yes'  line noise removal using discrete fourier transform  
          cfg.medianfilter  = 'no' or 'yes'  jump preserving median filter  
          cfg.lpfreq        = lowpass  frequency in Hz  
          cfg.hpfreq        = highpass frequency in Hz  
          cfg.bpfreq        = bandpass frequency range, specified as [low high] in Hz  
          cfg.bsfreq        = bandstop frequency range, specified as [low high] in Hz  
          cfg.dftfreq       = line noise frequencies for DFT filter, default [50 100 150] Hz  
          cfg.lpfiltord     = lowpass  filter order (default set in low-level function)  
          cfg.hpfiltord     = highpass filter order (default set in low-level function)  
          cfg.bpfiltord     = bandpass filter order (default set in low-level function)  
          cfg.bsfiltord     = bandstop filter order (default set in low-level function)  
          cfg.medianfiltord = length of median filter  
          cfg.lpfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'  
          cfg.hpfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'  
          cfg.bpfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'  
          cfg.bsfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'  
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
          cfg.demean        = 'no' or 'yes'  
          cfg.baselinewindow = [begin end] in seconds, the default is the complete trial  
          cfg.detrend       = 'no' or 'yes', this is done on the complete trial  
          cfg.polyremoval   = 'no' or 'yes', this is done on the complete trial  
          cfg.polyorder     = polynome order (default = 2)  
          cfg.derivative    = 'no' (default) or 'yes', computes the first order derivative of the data, using the MATLAB gradient function  
          cfg.hilbert       = 'no', 'abs', 'complex', 'real', 'imag', 'absreal', 'absimag' or 'angle' (default = 'no')  
          cfg.rectify       = 'no' or 'yes'  
          cfg.precision     = 'single' or 'double' (default = 'double')  
          cfg.absdiff       = 'no' or 'yes', computes absolute of the first order difference (i.e. first diff then rectify), using the MATLAB diff function  
         
        Preprocessing options that you should only use for EEG data are  
          cfg.reref         = 'no' or 'yes' (default = 'no')  
          cfg.refchannel    = cell-array with new EEG reference channel(s)  
          cfg.refmethod     = 'avg', 'median', 'rest', 'bipolar' or 'laplace' (default = 'avg')  
          cfg.groupchans    = 'yes' or 'no', should channels be rereferenced in separate groups  
                              for bipolar and laplace methods, this requires channnels to be  
                              named using an alphanumeric code, where letters represent the  
                              group and numbers represent the order of the channel whithin  
                              its group (default = 'no')  
          cfg.leadfield     = matrix or cell-array, this is required when refmethod is 'rest'  
                              The leadfield can be a single matrix (channels X sources) which  
                              is calculated by using the forward theory, based on the  
                              electrode montage, head model and equivalent source model.  
                              It can also be the output of FT_PREPARE_LEADFIELD based on a  
                              realistic head model.  
          cfg.implicitref   = 'label' or empty, add the implicit EEG reference as zeros (default = [])  
          cfg.montage       = 'no' or a montage structure (default = 'no')  
         
        See also FT_READ_DATA, FT_READ_HEADER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/preproc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("preproc", *args, **kwargs)
