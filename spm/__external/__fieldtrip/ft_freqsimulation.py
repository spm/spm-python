from spm.__wrapper__ import Runtime


def ft_freqsimulation(*args, **kwargs):
    """
      FT_FREQSIMULATION simulates channel-level time-series data . The data is built up  
        from different frequencies and can contain a signal in which the different  
        frequencies interact (i.e. cross-frequency coherent). Different methods are  
        possible to make data with specific properties.  
         
        Use as  
          [data] = ft_freqsimulation(cfg)  
        which will return a raw data structure that resembles the output of  
        FT_PREPROCESSING.  
         
        The configuration options can include  
          cfg.method     = The methods are explained in more detail below, but they can be  
                            'superimposed'    simply add the contribution of the different frequencies  
                            'broadband'       create a single broadband signal component  
                            'phalow_amphigh'  phase of low freq correlated with amplitude of high freq  
                            'amplow_amphigh'  amplitude of low freq correlated with amplithude of high freq  
                            'phalow_freqhigh' phase of low freq correlated with frequency of high signal  
                            'asymmetric'      single signal component with asymmetric positive/negative deflections  
          cfg.output     = which channels should be in the output data, can be 'mixed' or 'all' (default = 'all')  
          cfg.randomseed = 'yes' or a number or vector with the seed value (default = 'yes')  
         
        The number of trials and the time axes of the trials can be specified by  
          cfg.fsample    = simulated sample frequency (default = 1200)  
          cfg.trllen     = length of simulated trials in seconds (default = 1)  
          cfg.numtrl     = number of simulated trials (default = 1)  
          cfg.baseline   = number (default = 0)  
        or by  
          cfg.time       = cell-array with one time axis per trial, which are for example obtained from an existing dataset  
         
        For each of the methods default parameters are configured to generate  
        example data, including noise. To get full control over the generated  
        data you should explicitely set all parameters involved in the method  
        of your choise. The interpretation of the following signal components  
        depends on the specified method:  
         
        cfg.s1.freq     = frequency of signal 1  
        cfg.s1.phase    = phase (in rad) relative to cosine of signal 1  (default depends on method)  
                        = number or 'random'  
        cfg.s1.ampl     = amplitude of signal 1  
        cfg.s2.freq     = frequency of signal 2  
        cfg.s2.phase    = phase (in rad) relative to cosine of signal 1  (default depends on method)  
                        = number or 'random'  
        cfg.s2.ampl     = amplitude of signal 2  
        cfg.s3.freq     = frequency of signal 3  
        cfg.s3.phase    = phase (in rad) relative to cosine of signal 1  (default depends on method)  
                        = number or 'random'  
        cfg.s3.ampl     = amplitude of signal 3  
        cfg.s4.freq     = frequency of signal 4  
        cfg.s4.phase    = phase (in rad) relative to cosine of signal 1  (default depends on method)  
                        = number or 'random'  
        cfg.s4.ampl     = amplitude of signal 4  
         
        cfg.n1.ampl     = root-mean-square amplitude of wide-band signal prior to filtering  
        cfg.n1.bpfreq   = [Flow Fhigh]  
        cfg.n2.ampl     = root-mean-square amplitude of wide-band signal prior to filtering  
        cfg.n2.bpfreq   = [Flow Fhigh]  
         
        cfg.asymmetry   = amount of asymmetry (default = 0, which is none)  
        cfg.noise.ampl  = amplitude of noise  
         
         
        In the method 'superimposed' the signal contains just the sum of the different frequency contributions:  
            s1: first frequency  
            s2: second frequency  
            s3: third frequency  
        and the output consists of the following channels:  
            1st channel: mixed signal = s1 + s2 + s3 + noise  
            2nd channel: s1  
            3rd channel: s2  
            4th channel: s3  
            5th channel: noise  
         
        In the method 'broadband' the signal contains a the superposition of two  
        broadband signal components, which are created by bandpass filtering a  
        Gaussian noise signal:  
            n1: first broadband signal  
            n2: second broadband signal  
        and the output consists of the following channels:  
            1st channel: mixed signal = n1 + n2 + noise  
            2nd channel: n1  
            3rd channel: n2  
            4th channel: noise  
         
        In the method 'phalow_amphigh' the signal is build up of 4 components; s1, s2, s3 and noise:  
            s1: amplitude modulation (AM), frequency of this signal should be lower than s2  
            s2: second frequency, frequncy that becomes amplitude modulated  
            s3: DC shift of s1, should have frequency of 0  
        and the output consists of the following channels:  
            1st channel: mixed signal = (s1 + s3)*s2 + noise,  
            2nd channel: s1  
            3rd channel: s2  
            4th channel: s3  
            5th channel: noise  
         
        In the method 'amplow_amphigh' the signal is build up of 5 components; s1, s2, s3, s4 and noise.  
            s1: first frequency  
            s2: second frequency  
            s3: DC shift of s1 and s2, should have frequency of 0  
            s4: amplitude modulation (AM), frequency of this signal should be lower than s1 and s2  
        and the output consists of the following channels:  
            1st channel: mixed signal = (s4 + s3)*s1 + (s4 + s3)*s2 + noise,  
            2nd channel: s1  
            3rd channel: s2  
            4th channel: s3  
            5th channel: noise  
            6th channel: s4  
            7th channel: mixed part 1: (s4 + s3)*s1  
            8th channel: mixed part 2: (s4 + s3)*s2  
         
        In the method 'phalow_freqhigh' a frequency modulated signal is created.  
          signal is build up of 3 components; s1, s2 and noise.  
            s1: represents the base signal that will be modulated  
            s2: signal that will be used for the frequency modulation  
        and the output consists of the following channels:  
            1st channel: mixed signal = s1.ampl * cos(ins_pha) + noise  
            2nd channel: s1  
            3rd channel: s2  
            4th channel: noise  
            5th channel: inst_pha_base   instantaneous phase of the high (=base) frequency signal s1  
            6th channel: inst_pha_mod    low frequency phase modulation, this is equal to s2  
            7th channel: inst_pha        instantaneous phase, i.e. inst_pha_base + inst_pha_mod  
         
        In the method 'asymmetric' there is only one periodic signal, but that  
        signal is more peaked for the positive than for the negative deflections.  
        The average of the signal over time is zero.  
            s1: represents the frequency of the base signal  
        and the output consists of the following channels:  
            1st channel: mixed signal = asymmetric signal + noise  
            2nd channel: sine wave with base frequency and phase, i.e. s1  
            3rd channel: asymmetric signal  
            4th channel: noise  
         
        See also FT_FREQANALYSIS, FT_TIMELOCKSIMULATION, FT_DIPOLESIMULATION,  
        FT_CONNECTIVITYSIMULATION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_freqsimulation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_freqsimulation", *args, **kwargs)
