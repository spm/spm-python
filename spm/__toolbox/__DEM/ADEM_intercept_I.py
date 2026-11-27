from spm._runtime import Runtime


def ADEM_intercept_I(*args, **kwargs):
    r"""
      Radar tracking and interception in generalised coordinates of motion  
       __________________________________________________________________________  
        This is a simplified version of the interceptor demo, in which the gimbal  
        has a fixed orientation; thereby, reducing the latent states to the  
        position of the missile and drone. This enables action to be specified  
        directly as controlling velocity (rate of change of position) that is  
        projected into generalised coordinates of motion (here to 4th order).  
         
        In addition, this demo equips the drone with weaving behaviour modelled  
        in terms of a discrete sine set; i.e., parameterised by coefficients that  
        control variations in direction of travel as (sine) functions of distance  
        to target (i.e., the rendezvous point). It is assumed that these  
        coefficients are known or have been previously estimated based upon the  
        missiles early behaviour. The remaining latent cause — namely the target  
        — is inferred in the usual way; allowing, in principle, en route changes  
        to the target location.  
         
        The sensor signals are assumed to be sufficiently preprocessed to remove  
        random fluctuations that would otherwise confound generalised  
        observations. Uncertainty about these signals is therefore modelled in  
        terms of the precisions supplied to the generative model. These  
        precisions have to be specified carefully to ensure the sensory  
        attenuation of observations that can be changed via control. In other  
        words, the precision of IMU signals has to be smaller than the precision  
        used by the actuator for resolving prediction errors through action.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_intercept_I.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_intercept_I", *args, **kwargs, nargout=0)
