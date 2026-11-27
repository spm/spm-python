from spm._runtime import Runtime


def ADEM_intercept_III(*args, **kwargs):
    r"""
      Fixed wing interception in generalised coordinates of motion  
       __________________________________________________________________________  
        This version is for a fixed-wing interceptor. In brief, it uses a  
        combination of first order kinetics to approach the bomb in a moving  
        frame of reference. This moving frame of reference is modelled using the  
        second order dynamics based upon a hidden cause that pulls both the  
        interceptor and bomb to a common point, which is moving from towards the  
        target. This hidden causes equipped with smooth random fluctuations to  
        model countermeasures.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_intercept_III.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_intercept_III", *args, **kwargs, nargout=0)
