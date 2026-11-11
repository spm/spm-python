from spm._runtime import Runtime


def _continuous_ns(*args, **kwargs):
    r"""
      CONTINUOUS_NS created a trial definition from a Neuroscan *.cnt file  
        which subsequently can be used in the EEG/MEG framework  
         
        Use as  
          [trl] = continuous_ns(cfg)  
         
        where the configuration should contain   
          cfg.trialdef.trigger  = number or list with triggers  
          cfg.trialdef.prestim  = pre-stimulus in seconds  
          cfg.trialdef.poststim = post-stimulus in seconds      
         
        See also SINGLETRIAL_NS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/continuous_ns.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("continuous_ns", *args, **kwargs)
