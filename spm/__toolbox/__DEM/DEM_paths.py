from spm._runtime import Runtime


def DEM_paths(*args, **kwargs):
    r"""
     --------------------------------------------------------------------------  
        From densities to dynamics. This routine provides a numerical  
        illustration of how to construct a random dynamical system from a  
        probability density over some metric state-space. This involves sampling  
        a set of points from an inhomogeneous density and creating an ordered  
        list as follows: Add, without replacement, the point closest to the last  
        point added. Start with the point furthest from the origin and repeat,  
        until all points have been appended to the list. The ordered list can now  
        be treated as a time-series, describing a unique path through  
        state-space; namely, a time-homogenous Markov process. The implicit  
        movement through state space can now be decomposed into a part that can  
        be predicted given its position in state space, and a residual component,  
        using a least squares estimator of the movement (i.e., flow) at each  
        position. By construction, the residuals will have a zero mean Gaussian  
        distribution by central limit theorem. This follows because the predicted  
        flow is a linear mixture of some basis functions used for the least  
        squares estimation.  
         
        The ensuing decomposition can now be read as a random dynamical system,  
        apt for analysis in terms of pullback attractors (Arnold, 2003; Crauel  
        and Flandoli, 1994; Zaou et al., 2024) or, in a physics setting, a  
        Langevin formulation (Girolami and Calderhead, 2011; Kerr and Graham,  
        2000; Pavliotis, 2014; Seifert, 2012; Sekimoto, 1998). In the current  
        example, 2^12 points are sampled from a distribution over a  
        two-dimensional state-space—with a flat Euclidean geometry—supplied. The  
        functional form of the probability density, over the first state,  
        comprises two Gaussian distributions. The conditional density of the  
        second state was a quadratic function of the first.  
          
        The figure produced by this routine shows the sample points in the upper  
        right panel, and the accompanying timeseries are shown on the upper  
        right. These timeseries are rendered as a path--in the left middle  
        panel--as a succession of vectors that we can associate with motion.  
        Following least squares estimation of this motion--using fourth-order  
        polynomial basis functions of the two states--the predicted motion (i.e.,  
        flow) can be evaluated at each point (middle panel) and subtracted from  
        the motion to identify the residuals (right middle panel), that can be  
        treated as random fluctuations. Centring the fluctuations on their  
        expectation of zero discloses their Gaussian form (lower panels). This  
        construction associates time with some unique ordering of points sampled  
        from a metric state-space. The ensuing dynamics can have complicated  
        structure, as illustrated in the middle panel depicting flow as a vector  
        field.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_paths.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_paths", *args, **kwargs, nargout=0)
