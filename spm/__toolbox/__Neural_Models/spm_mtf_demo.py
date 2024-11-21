from spm.__wrapper__ import Runtime


def spm_mtf_demo(*args, **kwargs):
    """
      Demo routine for inverting local field potential models  
       ==========================================================================  
         
        This demonstrates the inversion of a simple DCM for spectral activity in  
        a single-source under steady-state assumptions; we use data reported  
        in:  
          
        Bayesian estimation of synaptic physiology from the spectral responses of  
        neural masses  
        Moran, R.J.1, Stephan K.E.,  Kiebel S.J., Rombach N., O'Connor  
        W.T., Murphy K.J., Reilly R.B., Friston K.J.  
          
        Abstract  
        We describe a Bayesian inference scheme for quantifying the active  
        physiology of neuronal ensembles using local field recordings of synaptic  
        potentials. This entails the inversion of a generative neural mass model  
        of steady-state spectral activity. The inversion uses Expectation  
        Maximization (EM) to furnish the posterior probability of key synaptic  
        parameters and the marginal likelihood of the model itself. The neural  
        mass model embeds prior knowledge pertaining to both the anatomical  
        [synaptic] circuitry and plausible trajectories of neuronal dynamics.  
        This model comprises a population of excitatory pyramidal cells, under  
        local interneuron inhibition and driving excitation from layer IV  
        stellate cells. Under quasi-stationary assumptions, the model can predict  
        the spectral profile of local field potentials (LFP).  This means model  
        parameters can be optimised given real electrophysiological observations.  
        The validity of inferences about synaptic parameters is demonstrated  
        using simulated data and experimental recordings from the medial  
        prefrontal cortex of control and isolation-reared Wistar rats.  
        Specifically, we examined the maximum a posteriori estimates of  
        parameters describing synaptic function in the two groups and tested  
        predictions derived from concomitant microdialysis measures. The  
        modelling of the LFP recordings revealed (i) a sensitization of  
        post-synaptic excitatory responses, particularly marked in pyramidal  
        cells, in the medial prefrontal cortex of socially isolated rats and (ii)  
        increased neuronal adaptation.  These inferences were consistent with  
        predictions derived from experimental microdialysis measures of  
        extracellular glutamate levels.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_mtf_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mtf_demo", *args, **kwargs, nargout=0)
