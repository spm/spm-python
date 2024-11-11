from spm.__wrapper__ import Runtime


def ADEM_cued_response(*args, **kwargs):
    """
      Cued responses under active inference:   
       __________________________________________________________________________  
        This demo illustrates cued sequential movements. It uses active inference  
        under a hierarchal generative model of sequential cues and consequent  
        movements. The agent has a (second level) model of (two) contingencies or  
        contexts; these correspond to the sequential appearance of targets in a  
        clockwise direction. The other context has no sequential aspect. The  
        first level model is contextually modulated to produce the appropriate  
        sequence of (location - specific) affordances, which predict both  
        visual and proprioceptive consequences. This is sufficient to engender  
        cued reaching movements, which are slightly anticipatory if the agent  
        infers the correct probabilistic context. However, if we reverse the  
        order of the stimuli there is an accuracy and reaction time cost, due to  
        the fact that the sequence is unpredictable.  Furthermore, there is a  
        set switching cost as the hidden states at the second (contextual) level  
        are inferred. This provides a simple but very rich model of cued reaching  
        movements and set switching that is consistent with notions of salience  
        and affordance. Furthermore, we can simulate Parkinsonism by  
        reducing the precision of affordance - based cues. These are the visual  
        attributes that confer saliency on the current target. Reducing this  
        precision (for example, dopamine) delays and can even preclude set  
        switching, with associated costs in pointing accuracy. By completely  
        removing the precision of the salience or affordance cues, we obtain  
        autonomous behaviour that is prescribed by the itinerant expectations of  
        the agent. This can be regarded as perseveration in a pathological  
        setting or the emission of autonomous behaviour in the absence of any  
        precise sensory information  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_cued_response.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_cued_response", *args, **kwargs, nargout=0)
