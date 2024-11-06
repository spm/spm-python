from spm.__wrapper__ import Runtime


def ft_artifact_zvalue(*args, **kwargs):
    """
      FT_ARTIFACT_ZVALUE scans data segments of interest for artifacts, by means of  
        thresholding the z-scored values of signals that have been preprocessed,  
        using heuristics that increase the sensitivity to detect certain types of artifacts.  
        Depending on the preprocessing options, this method will be sensitive to EOG, muscle   
        or SQUID jump artifacts. The z-scoring is applied in order to make the threshold  
        independent of the phsyical units in the data.  
         
        Use as  
          [cfg, artifact] = ft_artifact_zvalue(cfg)  
        with the configuration options  
          cfg.trl        = structure that defines the data segments of interest, see FT_DEFINETRIAL  
          cfg.continuous = 'yes' or 'no' whether the file contains continuous data.  
                           If the data has not been recorded continuously, then the cfg.trl should  
                           stricly observe the boundaries of the discontinuous segments, and the   
                           permitted values padding options (described below) are restricted to 0.   
          cfg.dataset    = string with the filename  
        or  
          cfg.headerfile = string with the filename  
          cfg.datafile   = string with the filename  
        and optionally  
          cfg.headerformat  
          cfg.dataformat  
         
        Alternatively you can use it as  
          [cfg, artifact] = ft_artifact_zvalue(cfg, data)  
        where the input data is a structure as obtained from FT_PREPROCESSING. Any preprocessing options  
        defined in the cfg will be applied to the data before the z-scoring and thresholding.  
         
        In both cases the configuration should also contain  
          cfg.trl        = structure that defines the data segments of interest, see FT_DEFINETRIAL  
          cfg.continuous = 'yes' or 'no' whether the file contains continuous data  
        and  
          cfg.artfctdef.zvalue.channel    = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details  
          cfg.artfctdef.zvalue.cutoff     = number, z-value threshold  
          cfg.artfctdef.zvalue.trlpadding = number in seconds  
          cfg.artfctdef.zvalue.fltpadding = number in seconds  
          cfg.artfctdef.zvalue.artpadding = number in seconds  
         
        If you encounter difficulties with memory usage, you can use  
          cfg.memory = 'low' or 'high', whether to be memory or computationally efficient, respectively (default = 'high')  
         
        The optional configuration settings (see below) are:  
          cfg.artfctdef.zvalue.artfctpeak       = 'yes' or 'no'  
          cfg.artfctdef.zvalue.artfctpeakrange  = [begin end]  
          cfg.artfctdef.zvalue.interactive      = 'yes' or 'no'  
          cfg.artfctdef.zvalue.zscore           = 'yes' (default) or 'no'     
         
        If you specify cfg.artfctdef.zvalue.artfctpeak='yes', a peak detection on the suprathreshold  
        z-scores will be performed, and the artifact will be defined relative to  
        the peak, where the begin and end points will be defined by  
        cfg.artfctdef.zvalue artfctpeakrange, rather than by the time points that  
        exceed the threshold.  
         
        You can specify cfg.artfctdef.zvalue.artfctpeakrange if you want to use the  
        detected artifacts as input to the DSS method of FT_COMPONENTANALYSIS. The result  
        is saved into cfg.artfctdef.zvalue.artifact. The range will automatically  
        respect the trial boundaries, i.e. it will be shorter if peak is near the beginning  
        or end of a trial. Samples between trials will be removed, thus this will not match  
        the sampleinfo of the data structure.  
         
        If you specify cfg.artfctdef.zvalue.zscore = 'no', the data will NOT be z-scored prior  
        to thresholding. This goes a bit against the name of the function, but it may be useful  
        if the threshold is to be defined in meaningful physical units, e.g. degrees of visual  
        angle for eye position data.  
         
        If you specify cfg.artfctdef.zvalue.interactive = 'yes', a graphical user interface  
        will show in which you can manually accept/reject the detected artifacts, and/or  
        change the threshold. To control the graphical interface via keyboard, use the  
        following keys:  
         
            q                 : Stop  
         
            comma             : Step to the previous artifact trial  
            a                 : Specify artifact trial to display  
            period            : Step to the next artifact trial  
         
            x                 : Step 10 trials back  
            leftarrow         : Step to the previous trial  
            t                 : Specify trial to display  
            rightarrow        : Step to the next trial  
            c                 : Step 10 trials forward  
         
            k                 : Keep trial  
            space             : Mark complete trial as artifact  
            r                 : Mark part of trial as artifact  
         
            downarrow         : Shift the z-threshold down  
            z                 : Specify the z-threshold  
            uparrow           : Shift the z-threshold down  
         
        Configuration settings related to the preprocessing of the data are  
          cfg.artfctdef.zvalue.lpfilter      = 'no' or 'yes'  lowpass filter  
          cfg.artfctdef.zvalue.hpfilter      = 'no' or 'yes'  highpass filter  
          cfg.artfctdef.zvalue.bpfilter      = 'no' or 'yes'  bandpass filter  
          cfg.artfctdef.zvalue.bsfilter      = 'no' or 'yes'  bandstop filter for line noise removal  
          cfg.artfctdef.zvalue.dftfilter     = 'no' or 'yes'  line noise removal using discrete fourier transform  
          cfg.artfctdef.zvalue.medianfilter  = 'no' or 'yes'  jump preserving median filter  
          cfg.artfctdef.zvalue.lpfreq        = lowpass  frequency in Hz  
          cfg.artfctdef.zvalue.hpfreq        = highpass frequency in Hz  
          cfg.artfctdef.zvalue.bpfreq        = bandpass frequency range, specified as [low high] in Hz  
          cfg.artfctdef.zvalue.bsfreq        = bandstop frequency range, specified as [low high] in Hz  
          cfg.artfctdef.zvalue.lpfiltord     = lowpass  filter order  
          cfg.artfctdef.zvalue.hpfiltord     = highpass filter order  
          cfg.artfctdef.zvalue.bpfiltord     = bandpass filter order  
          cfg.artfctdef.zvalue.bsfiltord     = bandstop filter order  
          cfg.artfctdef.zvalue.medianfiltord = length of median filter  
          cfg.artfctdef.zvalue.lpfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'  
          cfg.artfctdef.zvalue.hpfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'  
          cfg.artfctdef.zvalue.bpfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'  
          cfg.artfctdef.zvalue.bsfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'  
          cfg.artfctdef.zvalue.detrend       = 'no' or 'yes'  
          cfg.artfctdef.zvalue.demean        = 'no' or 'yes'  
          cfg.artfctdef.zvalue.baselinewindow = [begin end] in seconds, the default is the complete trial  
          cfg.artfctdef.zvalue.hilbert       = 'no' or 'yes'  
          cfg.artfctdef.zvalue.rectify       = 'no' or 'yes'  
         
        The output argument "artifact" is a Nx2 matrix comparable to the "trl" matrix of  
        FT_DEFINETRIAL. The first column of which specifying the beginsamples of an  
        artifact period, the second column contains the endsamples of the artifactperiods.  
         
        To facilitate data-handling and distributed computing, you can use  
          cfg.inputfile   =  ...  
        to read the input data from a *.mat file on disk. This mat files should contain  
        only a single variable named 'data', corresponding to the input structure.  
         
        See also FT_REJECTARTIFACT, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG, FT_ARTIFACT_EOG,  
        FT_ARTIFACT_JUMP, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_ZVALUE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_artifact_zvalue.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_artifact_zvalue", *args, **kwargs)
