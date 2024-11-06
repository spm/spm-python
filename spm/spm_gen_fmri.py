from spm.__wrapper__ import Runtime


def spm_gen_fmri(*args, **kwargs):
    """
      Generate a prediction of (multimodal) source activity  
        FORMAT [y,lfp,csd,w] = spm_gen_fmri(P,M,U)  
         
        P - parameters  
        M - neural-mass model structure  
        U - trial-effects  
          U.u  - inputs  
          U.dt - (micro) time bins for within-trial effects  
         
        y    - BOLD predictions (for every TR)  
        lfp  - voltages and conductances (for every micotime bin)  
        csd  - spectral density (for every TR)  
        w    - frequencies  
         
        This integration scheme returns a prediction of neuronal responses to  
        experimental inputs, in terms of BOLD responses and, if requested, local  
        field potentials and spectral density responses in each region or source.  
         
        The scheme uses a canonical microcircuit nneuron mass model of each  
        region to evaluate the new fixed point of neuronal activity every time  
        the input changes. This is evaluated in microtime (usually a 16th of the  
        TR). These neuronal states are then used to compute the pre-synaptic  
        activity of (extrinsic and intrinsic) afferents to each subpopulation to  
        furnish a neurovascular signal. The ensuing haemodynamic response is then  
        estimated by integrating a haemodynamic model. Neurovascular coupling  
        depends upon the mixtures of pre-synaptic activity driving haemodynamic  
        model. The associated weights are free parameters.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_gen_fmri.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gen_fmri", *args, **kwargs)
