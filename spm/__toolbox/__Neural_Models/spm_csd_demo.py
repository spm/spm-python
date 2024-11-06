from spm.__wrapper__ import Runtime


def spm_csd_demo(*args, **kwargs):
    """
      Demo routine for inverting local field potential models using  
        cross-spectral density summaries of steady-state dynamics  
       __________________________________________________________________________  
          
        This demo illustrates the inversion of neural-mass models (Moran et al  
        2005) of steady state-responses summarised in terms of the cross-spectral  
        density. These data features are extracted using a vector  
        auto-regression model and transformed into frequency space for subsequent  
        inversion using a biophysical neural-mass model that is parameterised in  
        terms of coupling and time constants.  
         
        One can generate exemplar data by integrating the neural-mass model or by  
        generating data directly from the cross-spectral DCM. In this demo we   
        use the former. DCM inversion using the standard nonlinear system   
        identification scheme spm_nlsi_N (a EM-like variational scheme under the   
        Laplace assumption).  
          
        NeuroImage. 2007 Sep 1;37(3):706-20.  
        A neural mass model of spectral responses in electrophysiology.Moran RJ,  
        Kiebel SJ, Stephan KE, Reilly RB, Daunizeau J, Friston KJ.   
         
        Abstract:  
        We present a neural mass model of steady-state membrane potentials  
        measured with local field potentials or electroencephalography in the  
        frequency domain. This model is an extended version of previous dynamic  
        causal models for investigating event-related potentials in the  
        time-domain. In this paper, we augment the previous formulation with  
        parameters that mediate spike-rate adaptation and recurrent intrinsic  
        inhibitory connections. We then use linear systems analysis to show how  
        the model's spectral response changes with its neurophysiological  
        parameters. We demonstrate that much of the interesting behaviour depends  
        on the non-linearity which couples mean membrane potential to mean  
        spiking rate. This non-linearity is analogous, at the population level,  
        to the firing rate-input curves often used to characterize single-cell  
        responses. This function depends on the model's gain and adaptation  
        currents which, neurobiologically, are influenced by the activity of  
        modulatory neurotransmitters. The key contribution of this paper is to  
        show how neuromodulatory effects can be modelled by adding adaptation  
        currents to a simple phenomenological model of EEG. Critically, we show  
        that these effects are expressed in a systematic way in the spectral  
        density of EEG recordings. Inversion of the model, given such  
        non-invasive recordings, should allow one to quantify pharmacologically  
        induced changes in adaptation currents. In short, this work establishes a  
        forward or generative model of electrophysiological recordings for  
        psychopharmacological studies.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_csd_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd_demo", *args, **kwargs, nargout=0)
