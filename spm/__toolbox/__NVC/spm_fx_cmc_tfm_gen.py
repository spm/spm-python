from spm.__wrapper__ import Runtime


def spm_fx_cmc_tfm_gen(*args, **kwargs):
    """
      Generate pre synaptic signals for multimodal DCM for fMRI and M/EEG  
        FORMAT [u,v,w]  = spm_fx_cmc_tfm_gen(x,u,P,M)  
        FORMAT [u,v]    = spm_fx_cmc_tfm_gen(x,u,P,M)  
        FORMAT [u]      = spm_fx_cmc_tfm_gen(x,u,P,M)  
         
        Inputs:  
        -------------------------------------------------------------------------  
        x      - state vector  
          x(:,1) - voltage     (spiny stellate cells)  
          x(:,2) - conductance (spiny stellate cells)  
          x(:,3) - voltage     (superficial pyramidal cells)  
          x(:,4) - conductance (superficial pyramidal cells)  
          x(:,5) - current     (inhibitory interneurons)  
          x(:,6) - conductance (inhibitory interneurons)  
          x(:,7) - voltage     (deep pyramidal cells)  
          x(:,8) - conductance (deep pyramidal cells)  
        P        - parameters of canonical micro circuits  
        u        - exogenous input  
        M        - neural-mass model structure  
        option   - options array for calculation pre synaptic signals {1 x 4}:  
          option{1} - 'pre' (pre synaptic) or 'de' (decomposed into intrinsic  
                      inhibitory, intrinsic excitatory and extrinsic excitatory)  
                      NVC drive.  
          option{2} - 'd' (different) or 's' (same) parameters of neurovascular   
                      scaling (this option is not used within this function).  
          option{3} - 'int' (only intrinsic neuronal signals are taken to account   
                      for simulating presynaptic signals) or 'ext' (external    
                      neuronal signals are additional included).  
          option{4} - EX, a 4x1 matrix  with either 0 or 1 elements (order as   
                      follows: [x(:,1) x(:,3) x(:,5) x(:,7)]) to exclude or    
                      include populations from calculation of pre synaptic signal  
         
         Examples of options               {'pre',   'd',    'int', EX},  
                                           {'pre',   's',    'int', EX},  
                                           {'pre',   'd',    'ext', EX},  
                                           {'pre',   's',    'ext', EX},  
                                           {'de',    's',    'int', EX},  
                                           {'de',    's',    'ext', EX},  
                                           {'de',    'd',    'int', EX},  
                                           {'de',    'd',    'ext', EX},  
         
        Outputs:  
        -------------------------------------------------------------------------  
         ux = spm_fx_cmc_tfm(x,u,P,M,option)  
         ux  -  simulated presynaptic signal (including or exclude distal regions)  
         
        [ux,vx] = spm_fx_cmc_tfm_gen(x,u,P,M,option)  
        ux  - intrinsic presynaptic input, (inhibitory)-without external input  
        vx  - intrinsic presynaptic input (excitatory)-without external input  
         
        [ux,vx,wx] = spm_fx_cmc_tfm_gen(x,u,P,M,,option)  
        ux  - intrinsic presynaptic input, (inhibitory)  
        vx  - intrinsic presynaptic input (excitatory)  
        wx  - extrinsic presynaptic input  
       --------------------------------------------------------------------------  
        Prior fixed parameter scaling [Defaults]  
         
        E  = (forward and backward) extrinsic rates  
        G  = intrinsic rates  
        D  = propagation delays (intrinsic, extrinsic)  
        T  = synaptic time constants  
        R  = slope of sigmoid activation function  
         
       __________________________________________________________________________  
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/NVC/spm_fx_cmc_tfm_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_cmc_tfm_gen", *args, **kwargs)
