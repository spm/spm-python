from spm.__wrapper__ import Runtime


def _chanscale_common(*args, **kwargs):
    """
      CHANSCALE_COMMON applies a scaling to specific channel types  
         
        Use as  
          data = chanscale_common(cfg, data)  
        where the configuration contains  
          cfg.parameter  
         
        For specific channel groups you can use  
          cfg.eegscale                = number, scaling to apply to the EEG channels prior to display  
          cfg.eogscale                = number, scaling to apply to the EOG channels prior to display  
          cfg.ecgscale                = number, scaling to apply to the ECG channels prior to display  
          cfg.emgscale                = number, scaling to apply to the EMG channels prior to display  
          cfg.megscale                = number, scaling to apply to the MEG channels prior to display  
          cfg.megrefscale             = number, scaling to apply to the MEG reference channels prior to display  
          cfg.magscale                = number, scaling to apply to the MEG magnetometer channels prior to display (in addition to the cfg.megscale factor)  
          cfg.gradscale               = number, scaling to apply to the MEG gradiometer channels prior to display (in addition to the cfg.megscale factor)  
          cfg.nirsscale               = number, scaling to apply to the NIRS channels prior to display  
         
        For individual control off the scaling for all channels you can use  
          cfg.chanscale               = Nx1 vector with scaling factors, one per channel specified in cfg.channel  
         
        For control over specific channels you can use  
          cfg.mychanscale             = number, scaling to apply to the channels specified in cfg.mychan  
          cfg.mychan                  = Nx1 cell-array with selection of channels  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/chanscale_common.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("chanscale_common", *args, **kwargs)
