from spm._runtime import Runtime


def ADEM_intercept_II(*args, **kwargs):
    r"""
      Radar tracking and interception in generalised coordinates of motion  
       __________________________________________________________________________  
        This iteration of the demo considers learning about the missile as a  
        prelude to online inference and tracking. The key move here is to observe  
        the missile (for 100 seconds) and estimate the (time-invariant)  
        parameters that govern its trajectory. These include things like the  
        speed, source, target and any parameters encoding evasive manoeuvres.  
        Crucially, these parameters are time-invariant and can be recovered using  
        dynamic expectation maximisation (DEM) from an observed timeseries. After  
        a sufficient period of observation, the parameters can then be used as  
        hidden causes for active inference and tracking as implemented in ADEM.  
        Note that these hidden causes can change from moment to moment because  
        causes are time-dependent variables. In this example, an initial missile  
        approach simulated until the missile is within 1 km of the line of  
        defence. It then reverts to a linear trajectory towards the target and  
        the gimbal infrared is engaged.   
         
        In addition, this demo allows for multiple radars and a re-factoring of  
        the subroutines that subtend the priors and likelihood mappings for the  
        generative process and model (where the behaviour of the missile is  
        shared by an observation model for off-line parameter estimation and the  
        generative model used for online tracking).  
          
        This demo accommodates conditional termination of the simulations  
        specified in DEM.break.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_intercept_II.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_intercept_II", *args, **kwargs, nargout=0)
