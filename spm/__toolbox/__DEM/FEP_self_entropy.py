from spm._runtime import Runtime


def FEP_self_entropy(*args, **kwargs):
    r"""
      This demonstration uses an ensemble of particles with intrinsic (Lorentz  
        attractor) dynamics and (Newtonian) short-range coupling.  This routine  
        illustrates self organisation in terms of the entropy of blanket states  
        (and concomitant changes in terms of mutual information (i.e., complexity  
        cost or risk). Here, the ensemble average of these entropy measures is  
        taken over all (128) particles of macromolecules; where the Markov  
        blanket of each particle comprises all but the third (electrochemical)  
        hidden state. The graphics produced by this routine simply plot the  
        decrease in blanket entropy (and complexity cost) as the system  
        approaches its random dynamical attractor. Illustrative trajectories of  
        the particles are provided at three points during the (stochastic)  
        chaotic transient.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/FEP_self_entropy.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("FEP_self_entropy", *args, **kwargs, nargout=0)
