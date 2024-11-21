from spm.__wrapper__ import Runtime


def spm_sigmoid_demo(*args, **kwargs):
    """
      Demo routine for neural mass models and the activation function  
        =========================================================================  
         
        This demo looks at the role of the sigmoid activation function in shaping  
        the impulse response of a neural-mass model. It uses Volterra kernels and  
        transfer functions and their dependency on the slope parameter of the  
        activation function; It is based on the paper by Marreiros et al :  
         
        Population dynamics: variance and the sigmoid activation function  
         
        Andre C. Marreiros, Jean Daunizeau, Stefan J. Kiebel, Karl J. Friston  
         
        Wellcome Trust Centre for Neuroimaging, University College London, United  
        Kingdom  
         
        Abstract  
         
        This paper demonstrates how the sigmoid activation function in  
        neural-mass models can be understood in terms of the variance or  
        dispersion of neuronal states.  We use this relationship to estimate the  
        probability density on hidden neuronal states, using non-invasive  
        electrophysiological (EEG) measures and dynamic casual modelling.  The  
        importance of implicit variance in neuronal states for neural-mass models  
        of cortical dynamics is illustrated using both synthetic data and real  
        EEG measurement of sensory evoked responses.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_sigmoid_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sigmoid_demo", *args, **kwargs, nargout=0)
