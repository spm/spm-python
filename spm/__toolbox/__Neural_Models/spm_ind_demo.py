from spm.__wrapper__ import Runtime


def spm_ind_demo(*args, **kwargs):
    """
      Demo for models of induced frequency responses and nonlinear coupling  
       ==========================================================================  
         
        This demo shows how the nonlinearity in a neural-mass model's sigmoid  
        activation function can induce cross-frequency coupling in the outputs.  
        In this demo [gamma] frequencies in the response are induced that are  
        not in the input. This is the basis of DCM for induced response where  
        nonlinear coupling is modelled as coupling between frequency modes. See  
        Chen et al for further details:  
          
        Dynamic causal modelling of induced responses  
          
        C.C. Chen, S.J. Kiebel, and K.J. Friston  
          
        ABSTRACT  
          
        This paper describes a dynamic causal model (DCM) for induced or spectral  
        responses as measured with the electroencephalogram (EEG) or the  
        magnetoencephalogram (MEG). We model the time-varying power, over a range  
        of frequencies, as the response of a distributed system of coupled  
        electromagnetic sources to a spectral perturbation. The model parameters  
        encode the frequency response to exogenous input and coupling among  
        sources and different frequencies. The Bayesian inversion of this model,  
        given data enables inferences about the parameters of a particular model  
        and allows us to compare different models, or hypotheses. One key aspect  
        of the model is that it differentiates between linear and nonlinear  
        coupling; which correspond to within and between-frequency coupling  
        respectively. To establish the face validity of our approach, we generate  
        synthetic data and test the identifiability of various parameters to  
        ensure they can be estimated accurately, under different levels of noise.  
        We then apply our model to EEG data from a face-perception experiment, to  
        ask whether there is evidence for nonlinear coupling between early visual  
        cortex and fusiform areas.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_ind_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ind_demo", *args, **kwargs, nargout=0)
