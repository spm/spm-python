from spm.__wrapper__ import Runtime


def DEMO_dcm_fmri_nnm(*args, **kwargs):
    """
      This demonstration routine illustrates the dynamic causal modelling of  
        fMRI timeseries using neural mass models. We first specify a simple DCM  
        for the attentional dataset. Following inversion, the posterior densities  
        are used to characterise the haemodynamic correlates of induced  
        responses.  
         
        This experiment involved attention to visual motion. We then use Bayesian  
        model reduction to ask whether attention was mediated through the  
        modulation of deep or superficial pyramidal cells in the visual motion  
        sensitive area (V5 or MST). in this setup, there are three regions and  
        three inputs (visual stimulation, visual motion and attention  to  
        motion). We treat the latter two inputs as modulatory; namely, increasing  
        extrinsic or intrinsic connectivity in particular parts of the network.  
        Intrinsic connectivity corresponds to the self-inhibition  of the (four)  
        neuronal populations constituting each region.  
         
        Finally, we address the contribution of extrinsic and intrinsic  
        pre-synaptic activity, laminar-specific contributions and the  
        contributions of  inhibitory interneurons to the BOLD signal. This  
        assessment uses Bayesian Model Reduction.  
         
          
       ==========================================================================  
         
        Options  
       --------------------------------------------------------------------------  
        DCM.options.two_state              % two regional populations (E and I)  
        DCM.options.stochastic             % fluctuations on hidden states  
        DCM.options.nonlinear              % interactions among hidden states  
        DCM.options.nograph                % graphical display  
        DCM.options.centre                 % mean-centre inputs  
        DCM.options.P                      % starting estimates for parameters  
        DCM.options.hidden                 % indices of hidden regions  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/DEMO_dcm_fmri_nnm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_dcm_fmri_nnm", *args, **kwargs)
