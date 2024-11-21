from spm.__wrapper__ import Runtime


def DEM_demo_contact_lens(*args, **kwargs):
    """
      This demo illustrates tracking under the contact lens problem:  
        The contact lens refers to the non-Gaussian uncertainty induced by  
        nonlinear measurements. Here it is illustrated in terms of tracking the  
        motion of a target in Cartesian coordinates, given the distance to target  
        (range) and direction as measurements. The problem is to accumulate  
        information over time about the target location under random fluctuations  
        on the velocity (technically this is a constant acceleration model).  
        Comparative evaluations are made with Extended Kalman filtering.  
         
        See: X. Tian, Y. Bar-Shalom, Coordinate Conversion and Tracking for   
        Very Long Range Radars. IEEE Transactions on Aerospace and Electronic  
        Systems, AES-45(3):1073-1088, July 2009.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_contact_lens.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_contact_lens", *args, **kwargs, nargout=0)
