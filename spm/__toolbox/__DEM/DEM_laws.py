from spm._runtime import Runtime


def DEM_laws(*args, **kwargs):
    r"""
      Demo of context sensitive preferences  
       __________________________________________________________________________  
          
        This demonstration script illustrates context-sensitive preferences and  
        the resolution of conflicting preferences under active inference. It  
        illustrates how one set of preferences (e.g., preferring not to violate  
        social or institutional norms) can be overwritten by potentially  
        conflicting preferences (e.g., preferred outcomes in an emergency), in  
        terms of choice behaviour. The particular setup considered here involves  
        moving from a starting location (e.g., the sidewalk) to a street crossing  
        and crossing the road, when a (green) walk sign allows. Crucially, a  
        siren can sound at any time, indicating an imperative to reach the other  
        side of the road. In nominal circumstances the agent will wait patiently  
        until the walk sign (i.e., deontic cue) switches from don't walk (red) to  
        walk (green). However, if the siren sounds, the agent could — with the  
        right preferences – cross the road, risking aversive outcomes; such as  
        being arrested or run over by a car.  
         
        In the example below, the agent has mild preferences for being at her  
        destination, which are not sufficient to overcome her aversion to  
        violations, unless she hears a siren. The don't walk sign (that can only  
        be seen from the crossing) is on for six timesteps. After four timesteps  
        the siren sounds and the agent infers there is an emergency. This compels  
        her to cross the road, thereby eliciting a violation but enabling her to  
        reach the safe destination. Interestingly, when the agent is sufficiently  
        confident there is an emergency — given an ambiguous (auditory)  
        likelihood mapping — she resolves her uncertainty about what to do,  
        eliciting a simulated phasic release of dopamine. This be regarded as  
        reporting the affective aspect of belief updating. Technically, dopamine  
        scores the increases or decreases in the average expected free energy  
        over policies; intuitively, this corresponds to the confidence in what  
        the agent — believes she — is doing.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_laws.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_laws", *args, **kwargs)
