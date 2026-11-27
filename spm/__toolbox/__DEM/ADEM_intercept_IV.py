from spm._runtime import Runtime


def ADEM_intercept_IV(*args, **kwargs):
    r"""
      Fixed wing interception in generalised coordinates of motion  
       __________________________________________________________________________  
        This version incorporates yaw, pitch and speed as states of the drone  
        such that action changes banking and speed (using a first order  
        approximation) to produce changes in velocity and Cartesian coordinates.  
        The model predicts velocity (i.e., changes in position) in Cartesian  
        coordinates using two components. The first is the velocity due to  
        attraction to the fixed point that is shared with the missile. The second  
        is a simple movement towards the missile. Inverting the implicit state  
        space model thereby precludes working in polar coordinates and the  
        nonlinearities (and discontinuities in angles) that would otherwise  
        confound variational inference. As in previous versions, action minimises  
        the prediction errors in position (as opposed to velocity).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_intercept_IV.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_intercept_IV", *args, **kwargs, nargout=0)
