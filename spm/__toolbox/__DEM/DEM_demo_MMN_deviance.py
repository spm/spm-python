from spm.__wrapper__ import Runtime


def DEM_demo_MMN_deviance(*args, **kwargs):
    """
      This Demo is a more refined illustration of the mismatch negativity that  
        uses a plausible (nonlinear) mapping from hidden states to sensory  
        samples; namely, a discrete spectral density (with a fixed frequency or  
        pitch tuning). This is modelled using a radial basis function over  
        frequencies, whose location parameter is a hidden state encoding pitch and  
        whose amplitude is modulated dynamically by hidden states encoding  
        amplitude modulation (the sum of two squared hidden states showing damped  
        linear oscillation when perturbed by a hidden cause). The recognition  
        dynamics illustrate a dissociation between the effects of changing the  
        (i) the level of deviancy of a stimulus (modelled here as a deviation of   
        the hidden state (cause) encoding pitch from zero) and (ii) the  
        probability of encountering a pitch deviant. This is modelled by changing  
        the precision on the hidden (pitch) state. Crucially, the nonlinearities  
        in this more plausible generative model of pure tone stimuli induce a  
        latency difference in the mismatch response and increase the amplitude  
        of the mismatch (i.e., MMN). Conversely, changing the precision only  
        affects the amplitude. In these simulations the MMN is modelled simply as  
        the difference between  prediction errors evoked by an expected stimulus  
        (the standard) and a deviant stimulus. Prior expectations are encoded  
        in terms of hidden causes, where the onset of the stimulus is known.  
        This means the agent has correct prior expectations about amplitude  
        modulation (i.e., knows when to expect a stimulus) but can have  
        incorrect expectations about its pitch (of varying confidence or  
        precision).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_MMN_deviance.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_MMN_deviance", *args, **kwargs, nargout=0)
