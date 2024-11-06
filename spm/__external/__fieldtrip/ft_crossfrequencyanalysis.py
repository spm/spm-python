from spm.__wrapper__ import Runtime


def ft_crossfrequencyanalysis(*args, **kwargs):
    """
      FT_CROSSFREQUENCYANALYSIS performs cross-frequency analysis  
         
        Use as  
          crossfreq = ft_crossfrequencyanalysis(cfg, freq)  
          crossfreq = ft_crossfrequencyanalysis(cfg, freqlo, freqhi)  
         
        The input data should be organised in a structure as obtained from the  
        FT_FREQANALYSIS function. The configuration should be according to  
         
          cfg.freqlow    = scalar or vector, selection of frequencies for the low frequency data  
          cfg.freqhigh   = scalar or vector, selection of frequencies for the high frequency data  
         
        Channel selection can be specified according to whether one wants to perform within- or  
        cross-channel analysis.  
         
        For within-channel analysis (default), you should specifies only a single channel selection:  
          cfg.channel    = cell-array with selection of channels, see FT_CHANNELSELECTION  
        In this case, the output "dimord" will be "chan_freqlow_freqhigh"  
         
        For cross-channel analysis, you should specifies two channel selections:  
          cfg.chanlow    = cell-array with selection of channels for the phase providing channels from the  
                           freqlow data argument, with wildcards allowed, see FT_CHANNELSELECTION  
          cfg.chanhigh   = cell-array with selection of channels for the amplitude providing channels from the  
                           freqhigh data argument, with wildcards allowed, see FT_CHANNELSELECTION  
        In this case, the output "dimord" will be "chancmb_freqlow_freqhigh" and "label"  
        field will be replaced with "labelcmb" (corresponding to the dimension "chancmb")  
        describing the pairs of channel combinations as  
          {'chanlow01' 'chanhigh01'  
           'chanlow01' 'chanhigh02'  
           ...  
           'chanlow02' 'chanhigh01'  
           'chanlow02' 'chanhigh02'  
           ...  
           }  
        N.B.: The order of channels corresponds to their order in the original "label" field  
         
        Various metrics for cross-frequency coupling have been introduced in a number of  
        scientific publications, but these do not use a consistent method naming scheme,  
        nor implement it in exactly the same way. The particular implementation in this  
        code tries to follow the most common format, generalizing where possible. If you  
        want details about the algorithms, please look into the code.  
          cfg.method     = string, can be  
                            'coh' - coherence  
                            'plv' - phase locking value  
                            'mvl' - mean vector length  
                            'mi'  - modulation index  
                            'pac' - phase amplitude coupling  
         
        The modulation index and phase amplitude coupling implement  
          Tort A. B. L., Komorowski R., Eichenbaum H., Kopell N. (2010). Measuring Phase-Amplitude  
          Coupling Between Neuronal Oscillations of Different Frequencies. J Neurophysiol 104:  
          1195?1210. doi:10.1152/jn.00106.2010  
         
        cfg.keeptrials = string, can be 'yes' or 'no'  
         
        See also FT_FREQANALYSIS, FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_crossfrequencyanalysis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_crossfrequencyanalysis", *args, **kwargs)
