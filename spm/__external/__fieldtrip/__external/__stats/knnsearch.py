from spm._runtime import Runtime


def knnsearch(*args, **kwargs):
    r"""
      KNNSEARCH finds the nearest neighbor in X for each point in Y.  
         
        This function serves as a drop-in replacement for the knnsearch function in the  
        stats toolbox.  
         
        Use as  
          indx = knnsearch(p1, p2)  
        where p1 and p2 are Nx3 and Mx3 matrices with vertices in 3D space. This returns a  
        Mx1 vector with indices that point into x.  
         
        the idea is that the distance between 2 points is:  
         
        sqrt(sum((p1(x,y,z)-p2(x,y,z)).^2)  
         
        since we are dealing with relative distances, we can get rid of the sqrt:  
        so we need to compute:  
         
        sum((p1(x,y,z)-p2(x,y,z)).^2)  
         
        this is the same as:  
         
        (p1x-p2x)^2 + (p1y-p2y)^2 + (p1z-p2z)^2  
         
        or, equivalently:  
         
        p1x^2 + p2x^2 - 2*p1x*p2x+ ...  
         
        reordering:  
         
        (p1x^2 + p1y^2 + p1z^2) + cross-terms + (p2x^2 + p2y^2 + p2z^2)  
         
        the last term between brackets is the same for each position-of-interest:  
        so it does not change the relative distance, and the first term between  
        brackets only needs to be computed once (below denoted as the 'offset'  
        variable.  
         
        See also DIST, DSEARCHN  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/stats/knnsearch.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("knnsearch", *args, **kwargs)
