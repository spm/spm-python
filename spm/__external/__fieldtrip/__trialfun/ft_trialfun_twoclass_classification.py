from spm.__wrapper__ import Runtime


def ft_trialfun_twoclass_classification(*args, **kwargs):
    """
      FT_TRIALFUN_TWOCLASS_CLASSIFICATION can be used to train and test a real-time  
        classifier in offline and online mode. It selects pieces of data in the two classes  
        based on two trigger values. The first N occurences in each class are marked as  
        training items. All subsequent occurrences are marked as test items.  
         
        This function can be used in conjunction with FT_REALTIME_CLASSIFICATION. The  
        configuration structure should contain  
          cfg.dataset              = string with the filename  
          cfg.trialfun             = 'ft_trialfun_twoclass_classification'  
          cfg.trialdef.numtrain    = number of training items, e.g. 20  
          cfg.trialdef.eventvalue1 = trigger value for the 1st class  
          cfg.trialdef.eventvalue2 = trigger value for the 2nd class  
          cfg.trialdef.eventtype   = string, e.g. 'trigger'  
          cfg.trialdef.prestim     = latency in seconds, e.g. 0.3  
          cfg.trialdef.poststim    = latency in seconds, e.g. 0.7  
         
        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_twoclass_classification.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_twoclass_classification", *args, **kwargs)
