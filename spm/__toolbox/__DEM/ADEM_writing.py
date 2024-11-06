from spm.__wrapper__ import Runtime


def ADEM_writing(*args, **kwargs):
    """
      This demo illustrates how action can fulfill prior expectations by   
        explaining away sensory prediction errors prescribed by desired movement   
        trajectories. In this example a two-joint arm follows a stable   
        heteroclinic channel, prescribed by a set of fixed point attractors. The   
        locations of the successive (autovitiated) attractors are defined by   
        parameters. The ensuing trajectories are illustrated here in terms of   
        synthetic writing.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_writing.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_writing", *args, **kwargs, nargout=0)
