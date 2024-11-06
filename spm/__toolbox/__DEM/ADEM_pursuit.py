from spm.__wrapper__ import Runtime


def ADEM_pursuit(*args, **kwargs):
    """
      Slow pursuit under active inference:   
       __________________________________________________________________________  
        This demo illustrates slow pursuit eye movements under active inference.   
        Its focus is on frames of references and the entrainment of gaze-  
        direction by the motion of a visual target. The generative process (and   
        model) is based upon the itinerant trajectory of a target (in Cartesian   
        coordinates) produced by Lotka-Volterra dynamics. The agent expects its   
        sampling (in polar coordinates) to be centred on the target. Here, the   
        agent is equipped with a model of the trajectory and the oculomotor   
        plant. This means it represents both the location of the target and the   
        mapping from target location (in relation to a fixation point) to   
        egocentric polar coordinates. We simulate behavioural (saccadic) and  
        electrophysiological (ERP) responses to expected and unexpected changes  
        in the direction of a target moving on the unit circle. The agent expects  
        the target to reverse its direction during the trajectory but when this  
        reversal is omitted (and the target) persists in a clockwise direction)  
        violation responses are emitted.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_pursuit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_pursuit", *args, **kwargs, nargout=0)
