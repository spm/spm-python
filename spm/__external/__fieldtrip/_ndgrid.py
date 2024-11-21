from spm.__wrapper__ import Runtime


def _ndgrid(*args, **kwargs):
    """
      NDGRID Generation of arrays for N-D functions and interpolation.  
        [X1,X2,X3,...] = NDGRID(x1,x2,x3,...) transforms the domain  
        specified by vectors x1,x2,x3, etc. into arrays X1,X2,X3, etc. that  
        can be used for the evaluation of functions of N variables and N-D  
        interpolation.  The i-th dimension of the output array Xi are copies  
        of elements of the vector xi.  
         
        [X1,X2,...] = NDGRID(x) is the same as [X1,X2,...] = NDGRID(x,x,...).  
         
        For example, to evaluate the function  x2*exp(-x1^2-x2^2-x^3) over the  
        range  -2 < x1 < 2,  -2 < x2 < 2, -2 < x3 < 2,  
         
            [x1,x2,x3] = ndgrid(-2:.2:2, -2:.25:2, -2:.16:2);  
            z = x2 .* exp(-x1.^2 - x2.^2 - x3.^2);  
            slice(x2,x1,x3,z,[-1.2 .8 2],2,[-2 -.2])  
         
        NDGRID is like MESHGRID except that the order of the first two input  
        arguments are switched (i.e., [X1,X2,X3] = NDGRID(x1,x2,x3) produces  
        the same result as [X2,X1,X3] = MESHGRID(x2,x1,x3)).  Because of  
        this, NDGRID is better suited to N-D problems that aren't spatially  
        based, while MESHGRID is better suited to problems in cartesian  
        space (2-D or 3-D).  
         
        This is a drop-in replacement for the MATLAB version in elmat, which is  
        relatively slow for big grids. Note that this function only works up  
        to 5 dimensions  
         
        See also MESHGRID, INTERPN.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/ndgrid.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ndgrid", *args, **kwargs)
