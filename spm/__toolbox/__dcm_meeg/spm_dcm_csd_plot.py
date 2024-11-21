from spm.__wrapper__ import Runtime


def spm_dcm_csd_plot(*args, **kwargs):
    """
      Plot the conditional density of coherence etc for a given connection  
        FORMAT spm_dcm_csd_plot(DCM,i,j,C)  
         
        DCM - inverted DCM structure for CSD models  
        i   - target source (or channel mode)  
        j   - source source (or channel mode)  
        C   - flag for channels (as opposed to sources  
         
        This routine is a graphics routine that plots the Bayesian confidence   
        tubes around cross-covariance, coherence and phase delays as functions   
        of lag and frequency. It also plots the conditional density over the   
        delay. The confidence tubes (Bayesian confidence intervals) are   
        approximated by sampling the underlying parameters from the   
        [approximate] conditional density.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_csd_plot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_csd_plot", *args, **kwargs, nargout=0)
