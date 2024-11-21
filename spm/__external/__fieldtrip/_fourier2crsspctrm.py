from spm.__wrapper__ import Runtime


def _fourier2crsspctrm(*args, **kwargs):
    """
      FOURIER2CRSSPCTRM transforms a fourier-containing freq-structure   
        into a crsspctrm-containing freq-structure, in which the  
        powerspectra are also contained in the cross-spectra, being a   
        channelcombination of a channel with itself.  
         
        Use as  
          [freq] = fourier2crsspctrm(cfg, freq)  
         
        where you have the following configuration options:  
          cfg.channel    = cell-array with selection of channels,  
                           see CHANNELSELECTION for details  
          cfg.channelcmb = cell-array with selection of combinations between  
                           channels, see CHANNELCOMBINATION for details  
          cfg.keeptrials = 'yes' or 'no' (default)  
          cfg.foilim     = 2-element vector defining your frequency limits of   
                           interest. By default the whole frequency range of the   
                           input is taken.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/fourier2crsspctrm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fourier2crsspctrm", *args, **kwargs)
