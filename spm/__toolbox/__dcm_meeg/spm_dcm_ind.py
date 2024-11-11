from spm.__wrapper__ import Runtime


def spm_dcm_ind(*args, **kwargs):
    """
      Estimate parameters of a (bilinear) DCM of induced spectral responses  
        FORMAT DCM = spm_dcm_ind(DCM)     
         
        DCM       
           name: name string  
              M:  Forward model  
                     M.dipfit - leadfield specification  
              xY: data   [1x1 struct]  
              xU: design [1x1 struct]  
         
          Sname: cell of source name strings  
              A: {[nr x nr double]  [nr x nr double]  [nr x nr double]}  
              B: {[nr x nr double], ...}   Connection constraints  
              C: [nr x 1 double]  
         
          options.Nmodes       - number of frequency modes  
          options.Tdcm         - [start end] time window in ms  
          options.D            - time bin decimation       (usually 1 or 2)  
          options.h            - number of DCT drift terms (usually 1 or 2)  
          options.type         - 'ECD' (1) or 'Imaging' (2) (see spm_erp_L)  
          options.onset        - stimulus onset (ms)  
          options.dur          - and dispersion (sd)  
       __________________________________________________________________________  
        This routine inverts dynamic causal models (DCM) of induced or spectral   
        responses as measured with the electroencephalogram (EEG) or the   
        magnetoencephalogram (MEG). It models the time-varying power, over a   
        range of frequencies, as the response of a distributed system of coupled   
        electromagnetic sources to a spectral perturbation. The model parameters   
        encode the frequency response to exogenous input and coupling among   
        sources and different frequencies. Bayesian inversion of this model,   
        given data enables inferences about the parameters of a particular model   
        and allows one to compare different models, or hypotheses. One key aspect   
        of the model is that it differentiates between linear and non-linear   
        coupling; which correspond to within and between frequency coupling   
        respectively.  
          
        The number of nodes can be optimised using Bayesian model selection. The  
        data are reduced to a fixed number of principal components that capture  
        the greatest variation inspection responses never peristimulus time. The  
        number of nodes specified by the user tries to reconstruct the response  
        in the space of the principle components or eigenmodes using a reduced  
        set of eigenmodes. The number of modes corresponding to data features can  
        be changed (from Nf = 8) by editing spm_dcm_ind_data.m  
         
        see also: spm_dcm_ind_data; spm_gen_ind; spm_fx_ind and spm_lx_ind  
          
        See: Chen CC, Kiebel SJ, Friston KJ.  
        Dynamic causal modelling of induced responses.  
        Neuroimage. 2008 Jul 15;41(4):1293-312.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_ind.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_ind", *args, **kwargs)
