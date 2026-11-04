from spm._runtime import Runtime


def spm_opm_ssp(*args, **kwargs):
    r"""
      Removes eignevectors of training data covaraince from test data  
        FORMAT D = spm_opm_ssp(S)  
          S               - input structure  
         fields of S:  
          S.trainD    - SPM MEEG object         - Default: no Default  
          S.testD     - SPM MEEG object         - Default: training data  
          S.trainwin  - Training Epoch (s)      - Default: [0,Inf]  
          S.testwin   - Testing Epoch (s)       - Default: [0,Inf]  
          S.ncomp     - Number of eigenvectors  - Default: 8  
          S.weights   - Channel weighting       - Default: ones(1,nchannels)  
          S.hp        - high pass filter (Hz)   - Default: no filter  
          S.lp        - low pass filter  (Hz)   - Default: no filter  
          S.notch     - Notch filter (Hz)       - Default: no filter  
        Output:  
          D               - denoised MEEG object (also written to disk)  
       __________________________________________________________________________  
        Copyright  Tim Tierney  
         
        Example   
        S=[];  
        S.trainD =D;                        % D object  
        S.testD = D;                        % D object(potentially different);  
        S.trainwin = [1,60];                % epochs   
        S.testwin = [61,Inf];               % epochs        
        S.ncomp = 32;                       % number of eigenvectors  
        S.weights  =ones(1,length(megind)); % vector of weights(1 for each channel)  
        S.weights(t2inds)= 1/6^2;           % e.g factor of six difference in noise floor  
        S.lp=[100];                         % filter only pplied to training data  
        S.hp=[1];                           % filter only pplied to training data  
        S.notch = [47 53;97 103];           % filter only pplied to training data  
        sspD = spm_opm_ssp(S);  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_opm_ssp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_opm_ssp", *args, **kwargs)
