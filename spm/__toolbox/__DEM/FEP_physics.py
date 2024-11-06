from spm.__wrapper__ import Runtime


def FEP_physics(*args, **kwargs):
    """
      This demonstration  uses an ensemble of particles with intrinsic (Lorenz  
        attractor) dynamics and (Newtonian) short-range coupling. the setup is  
        used to solve for dynamics among an ensemble of particles; from which a  
        Markov blanket emerges (which forms a particle at the next hierarchical  
        scale. These ensemble dynamics are then used to illustrate different  
        perspectives; namely, those afforded by quantum, statistical and  
        classical mechanics. A detailed description of each of these three  
        treatments precedes each of the sections in the script. these  
        descriptions are in the form of a figure legend, where each section is  
        summarised with a figure.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/FEP_physics.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("FEP_physics", *args, **kwargs, nargout=0)
