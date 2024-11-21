from spm.__wrapper__ import Runtime


def ft_steadystatesimulation(*args, **kwargs):
    """
      FT_STEADYSTATESIMULATION creates a simulated EEG/MEG dataset. This function  
        allows to simulate the effect of several independent stimulus trains. These can  
        be presented as a periodic sequence, or as single (or few) transient stimuli.  
        This function creates a single block of data. You can call it repeatedly and use  
        FT_APPENDDATA to combine different blocks.  
         
        Use as  
          data = ft_steadystatesimulation(cfg)  
        where cfg is a configuration structure that should contain  
          cfg.fsample    = scalar, sampling frequency in Hz (default = 512)  
          cfg.duration   = scalar, trial length in seconds (default = 4.56)  
          cfg.baseline   = scalar, baseline length in seconds (default = 0)  
          cfg.ntrials    = integer N, number of trials (default = 320)  
          cfg.iti        = scalar, inter-trial interval in seconds (default = 1)  
          cfg.randomseed = 'yes' or a number or vector with the seed value (default = 'yes')  
         
        Each trial can contain multiple nested experimental manipulations  
          cfg.level1.condition = scalar, or vector of length L1 (default = 1)  
          cfg.level1.gain      = scalar, or vector of length L1 (default = 1)  
          cfg.level2.condition = scalar, or vector of length L2 (default = 1)  
          cfg.level2.gain      = scalar, or vector of length L2 (default = 1)  
          cfg.level3.condition = scalar, or vector of length L3 (default = 1)  
          cfg.level3.gain      = scalar, or vector of length L3 (default = 1)  
        If you don't need level 2 and up, specify the condition and gain as empty.  
        Idem for level 3 and up.  
         
        Stimuli are created at the lowest experimental level, and are modulated according to the product of the gain of all levels.  
        Each trial can contain one or multiple stimuli.  
        The behavior of each stimuli is specified with  
          cfg.stimulus1.mode = 'periodic', 'transient' or 'off' (default = 'periodic')  
          cfg.stimulus2.mode = 'periodic', 'transient' or 'off' (default = 'transient')  
         
        If the stimulus is periodic (below as example for stimulus1), the following options apply  
          cfg.stimulus1.number          = does not apply for periodic stimuli  
          cfg.stimulus1.onset           = in seconds, first stimulus relative to the start of the trial (default = 0)  
          cfg.stimulus1.onsetjitter     = in seconds, max jitter that is added to the onset (default = 0)  
          cfg.stimulus1.isi             = in seconds, i.e. for 10Hz you would specify 0.1 seconds as the interstimulus interval (default = 0.1176)  
          cfg.stimulus1.isijitter       = in seconds, max jitter relative to the previous stimulus (default = 0)  
          cfg.stimulus2.condition       = does not apply for periodic stimuli  
          cfg.stimulus2.gain            = does not apply for periodic stimuli  
          cfg.stimulus1.kernelshape     = 'sine'  
          cfg.stimulus1.kernelduration  = in seconds (default = isi)  
         
        If the stimulus is transient (below as example for stimulus2), the following options apply  
          cfg.stimulus2.number          = scalar M, how many transients are to be presented per trial (default = 4)  
          cfg.stimulus2.onset           = in seconds, first stimulus relative to the start of the trial (default = 0.7)  
          cfg.stimulus2.onsetjitter     = in seconds, max jitter that is added to the onset (default = 0.2)  
          cfg.stimulus2.isi             = in seconds as the interstimulus interval (default = 0.7)  
          cfg.stimulus2.isijitter       = in seconds, max jitter relative to the previous stimulus (default = 0.2)  
          cfg.stimulus2.condition       = 1xM vector with condition codes for each transient within a trial (default = [1 1 2 2])  
          cfg.stimulus2.gain            = 1xM vector with gain for each condition for each transient within a trial (default = [1 1 1 1])  
          cfg.stimulus2.kernelshape     = 'hanning'  
          cfg.stimulus2.kernelduration  = in seconds (default = 0.75*isi)  
         
        RANDOMIZATIONS:  
        - The onsetjitter is randomized between 0 and the value given, and is always added to the onset.  
        - The isijitter is randomized between 0 and the value given, and is always added to the interstimulus interval (isi).  
        - For periodic stimuli, which are constant within a trial, the condition code and gain are shuffled over all trials.  
        - For transient stimuli, the condition code and gain are shuffled within each trial.  
         
        Using the default settings, we model a peripherally presented flickering stimulus  
        that appears at different excentricities together with a centrally presented  
        transient stimulus that appears 4x per trial. To simulate the experiment described  
        at , you have to call this 4 times with a different cfg.configuration and  
        cfg.gain to model the task load and use FT_APPENDDATA to concatenate the trials. In  
        this case cfg.condition models the factor "task load" (2 levels, low and high),  
        cfg.stimulus1.condition models the factor "excentricity" (4 levels), and  
        cfg.stimulation2.condition models the factor "stimulus type" (2 levels, non-target  
        or target).  
         
        See also FT_DIPOLESIMULATION, FT_TIMELOCKSIMULATION, FT_FREQSIMULATION,  
        FT_CONNECTIVITYSIMULATION, FT_APPENDDATA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_steadystatesimulation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_steadystatesimulation", *args, **kwargs)
