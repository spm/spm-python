from spm.__wrapper__ import Runtime


def _continuous_ns(*args, **kwargs):
    """
      CONTINUOUS_NS created a trial definition from a Neuroscan *.cnt file  
        which subsequently can be used in the EEG/MEG framework  
         
        Use as  
          [trl] = continuous_ns(cfg)  
         
        where the configuration should contain   
          cfg.trialdef.trigger  = number or list with triggers  
          cfg.trialdef.prestim  = pre-stimulus in seconds  
          cfg.trialdef.poststim = post-stimulus in seconds      
         
        See also SINGLETRIAL_NS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/continuous_ns.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("continuous_ns", *args, **kwargs)
