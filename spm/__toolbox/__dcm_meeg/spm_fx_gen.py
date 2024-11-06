from spm.__wrapper__ import Runtime


def spm_fx_gen(*args, **kwargs):
    """
      Generic state equations for a neural mass models  
        FORMAT [f,J,D] = spm_fx_gen(x,u,P,M)  
        FORMAT [f,J]   = spm_fx_gen(x,u,P,M)  
        FORMAT [f]     = spm_fx_gen(x,u,P,M)  
        x  - neuronal states  
        u  - exogenous input  
        P  - model parameters  
        M  - model structure  
         
        This routine compiles equations of motion for multiple nodes or neural  
        masses in the cell array of hidden states. To include a new sort of node,  
        it is necessary to update the following routines:  
          
        spm_dcm_neural_priors: to specify the intrinsic parameters of a new model  
        spm_dcm_x_neural:      to specify its initial states  
        spm_L_priors:          to specify which hidden states generate signal  
        spm_fx_gen (below):    to specify how different models interconnect  
         
        This routine deal separately with the coupling between nodes (that depend  
        upon extrinsic connectivity, sigmoid activation functions and delays -  
        and coupling within nodes (that calls on the model specific equations of  
        motion).  
         
        In generic schemes one can mix and match different types of sources;  
        furthermore, they can have different condition-specific modulation of  
        intrinsic connectivity parameters and different, source-specific-  
        contribution to the lead field (or electrode gain). Source-specific  
        models are specified by a structure array model, For the i-th source:  
         
        model(i).source  = 'ECD','CMC',...  % source model  
        model(i).B       = [i j k ,...]     % free parameters that have B effects  
        model(i).J       = [i j k ,...]     % cardinal states contributing to L  
        model(i).K       = [i j k ,...]     % other states contributing to L  
        ...  
       __________________________________________________________________________  
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fx_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_gen", *args, **kwargs)
