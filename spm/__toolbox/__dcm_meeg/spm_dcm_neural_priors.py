from spm.__wrapper__ import Runtime


def spm_dcm_neural_priors(*args, **kwargs):
    """
      Prepare the priors on the parameters of neural mass models  
        FORMAT [pE,pC] = spm_dcm_neural_priors(A,B,C,'model'))  
         
        A,B{m},C  - binary constraints on extrinsic connections for m conditions  
        'model'   - 'ERP','SEP','CMC','LFP','NNM' or 'MFM'  
         
        pE - prior expectation - f(x,u,P,M)  
         
        synaptic parameters (for NMN and MFM)  
       --------------------------------------------------------------------------  
           pE.T - synaptic time constants  
           pE.H - synaptic densities  
           pE.S - activation function parameters  
         
        connectivity parameters  
       --------------------------------------------------------------------------  
           pE.A  - extrinsic  
           pE.B  - trial-dependent  
           pE.C  - stimulus input  
         
           pE.D  - delays  
         
        stimulus and noise parameters  
       --------------------------------------------------------------------------  
           pE.R - onset and dispersion  
           pE.U - endogenous activity  
         
        pC - prior (co)variances  
         
        Because priors are specified under log normal assumptions, most  
        parameters are simply scaling coefficients with a prior expectation  
        and variance of one.  After log transform this renders pE = 0 and  
        pC = 1;  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_neural_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_neural_priors", *args, **kwargs)
