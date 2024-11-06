from spm.__wrapper__ import Runtime


def _ft_singletrialanalysis_aseo(*args, **kwargs):
    """
      FT_SINGLETRIALANALYSIS_ASEO executes single-trial analysis, using the ASEO  
        algorithm (Xu et al, 2009)  
         
        Use as  
          [output] = ft_singletrialanalysis_aseo(cfg, data_fft, erp_fft)  
        where data_fft is the observed data in the frequency domain, erp_fft  
        contains the initial ERP components in the frequency domain. cfg is a  
        configuration structure according to  
         
        OUTPUT----  
        amp_est    : Estimates of ERP components' amplitude  
        lat_est    : Estimates of ERP components' latency  
        erp_est    : Estimates of ERP waveforms in time domain  
        ar         : Estimated AR coefficients of on-going activity  
        noise      : Power spectrum of on-going activity fitted in AR model  
        sigma      : Power of the input white noise of AR model for on-going activity  
        residual   : Residual signal after removing ERPs in time domain  
        rejectflag : Each element of rejectflag indicating that the corresponding  
                     trial should be rejected or not. For example, rejectflag(9)==1 means  
                     the 9th trial is rejected.  
        corr_est    : Correlation between the original data and the recovered signal  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/ft_singletrialanalysis_aseo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_singletrialanalysis_aseo", *args, **kwargs)
