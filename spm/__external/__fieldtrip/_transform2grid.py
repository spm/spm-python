from spm._runtime import Runtime


def _transform2grid(*args, **kwargs):
    r"""
      TRANSFORM2GRID ensures that the volume contains the definition of the  
        cardian axes, i.e. xgrid/ygrid/zgrid. If the voluyme contains a  
        homogenous coordinate transformation axis that is unequal to eye(4), it  
        will try to construct the cardinal axis from that transformation matrix.  
         
        See also GRID2TRANSFORM  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/transform2grid.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("transform2grid", *args, **kwargs)
