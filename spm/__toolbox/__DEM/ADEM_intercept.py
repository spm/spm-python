from spm._runtime import Runtime


def ADEM_intercept(*args, **kwargs):
    r"""
      Radar tracking and interception in generalised coordinates of motion  
       __________________________________________________________________________  
        This script illustrates the use of generalised filtering to solve the  
        dual problem of radar tracking and interception. This is an elemental  
        instance of (mere) active inference in which the priors over dynamics are  
        realised through action. In this instance, the priors over latent states  
        induce a dynamics with a particular fixed point; namely, a drone lies on  
        the trajectory of a missile. It has an infrared sensor that points  
        towards the oncoming missile and, crucially, the angular velocity of its  
        gimbal mounted sensor is zero. The only situation in which these  
        conditions are met is when the drone is on the path of an approaching  
        missile. Writing down the equations of motion of the drone—with the above  
        solution— effectively creates a generative model of a drone that, a  
        priority, expects to intercept a missile. Conceptually, this can be read  
        as an instance of the equilibrium point hypothesis for motor control in  
        neurobiology. In economics, this would be regarded as a particular kind  
        of prior; i.e., a heuristic. In control theory, this is a special  
        instance of path integral control.  
         
        In detail, the generative process (and model) involves three objects and  
        a hidden cause. The first object is a missile travelling at a constant  
        velocity (135 km/h towards a target or rendezvous point in some line of  
        defence. This rendezvous point is the hidden cause. The second object is  
        a drone that is attracted to the rendezvous point with a maximum speed  
        (of 85 km/h). The third object is a (fixed location) radar that returns  
        precise estimates of the missile’s range and bearing (in terms of log  
        distance and radians, respectively). The drone is equipped with a  
        gimbal-mounted IR camera that reports the bearing of the missile when  
        sufficiently close. The drone’s IMU provides estimates of the drone’s  
        velocity and current position, along with the angle and angular velocity  
        of the gimbal. The active states of the drone effectively resolve IMU  
        (c.f., proprioceptive) prediction errors based upon the predictions of  
        the drone's dynamics and its gimbal.  
         
        Intuitively, one can regard the hidden cause as setting the direction of  
        travel for the missile and drone: to a common (rendezvous) point in a  
        fixed line of defence. Initially, the radar tracking supplies a posterior  
        estimate of the hidden cause and thereby attracts the drone to the  
        intercept position. As the missile comes into the range of the drone’s  
        infrared camera, posterior uncertainty about the hidden cause is  
        resolved. In addition, the drone manoeuvres along the defence line to  
        ensure its gimbal is pointing in the fixed direction of the oncoming  
        missile.  
         
        The inversion of the implicit continuous state-space model is in  
        generalised coordinates of motion. To attain the requisite accuracy  
        (i.e., centimetres) it is necessary to use relatively high orders of  
        generalised motion (here, 8). This setup is very sensitive to the  
        precisions of random fluctuations (and the relative estimates of these  
        precisions used during generalised filtering or state estimation). In the  
        example below, we have simplified the problem to 2 dimensions and have  
        used very precise radar and IMU signals to demonstrate what could be  
        achieved under realistic speeds and distances.  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_intercept.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_intercept", *args, **kwargs, nargout=0)
