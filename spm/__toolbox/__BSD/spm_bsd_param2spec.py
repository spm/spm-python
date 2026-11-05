from spm._runtime import Runtime


def spm_bsd_param2spec(*args, **kwargs):
    r"""
      Convert BSD model parameters to spectral parameters structure  
        FORMAT spec = spm_bsd_param2spec(P, M)  
         
        P   - structure containing model parameters:  
              .a : log-amplitude parameters  
              .f : frequency parameters  
              .S : log-FWHM (full width at half maximum) parameters  
              .b : log-noise parameters  
         
        M   - structure containing prior values:  
              .pV.f : [Nx2] matrix, prior frequency bounds (Hz)  
              .pV.S : prior FWHM scaling  
              .pV.b : prior noise scaling  
         
        spec - output structure containing spectral parameters:  
              .ampl : amplitude (exp-transformed from P.a)  
              .freq : frequency (transformed from P.f and prior bounds)  
              .fwhm : FWHM (derived from P.S and prior scaling)  
              .noise: noise (exp-transformed from P.b and prior scaling)  
         
        This function maps the parameter estimates from a Bayesian Spectral  
        Decomposition (BSD) model to a structure of spectral parameters for  
        further analysis or model evaluation.  
         
       _______________________________________________________________________  
        Copyright (C) 2024-2025 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/BSD/spm_bsd_param2spec.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bsd_param2spec", *args, **kwargs)
