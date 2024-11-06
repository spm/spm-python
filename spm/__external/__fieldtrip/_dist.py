from spm.__wrapper__ import Runtime


def _dist(*args, **kwargs):
    """
      DIST computes the Euclidian distance between the columns of the input matrix or  
        between the rows and columns of two input matrices.  
         
        This function serves as a drop-in replacement for the dist function in the Neural  
        Networks toolbox.  
         
        Use as  
          [d] = dist(x')  
        where x is for example an Nx3 matrix with vertices in 3D space, or as  
          [d] = dist(x, y')  
        where x and y are Nx3 and Mx3 matrices with vertices in 3D space  
         
        See also DSEARCHN, KNNSEARCH  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/dist.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("dist", *args, **kwargs)
