from spm.__wrapper__ import Runtime


def spm_get_closest_affine(*args, **kwargs):
    """
      Determine the affine transform mapping x to y  
        FORMAT [M,R] = spm_get_closest_affine(X,Y,W)  
        X  - n1*n2*n3*3 array of floats representing coordinates.  
        Y  - n1*n2*n3*3 array of floats representing coordinates.  
        W  - n1*n2*n3   array of floats representing weights.  
         
        M  - an affine transform  
        R  - a rigid-body transform  
         
        The code treats X and Y as reshaped versions (n1*n2*n3) x 3,  
        and W as a column vector.  
          
        It generates XX = [X 1]'*diag(W)*[X 1]  
        and          XY = [X 1]'*diag(W)*[Y 1]  
          
        These can then be used to compute an affine transform (M),  
        by M = (XX\XY)'  
        A weighted procrustes decomposition is also performed,  
        so that a rigid-body transform matrix (R) is returned.  
         
        If W is empty or not passed, then it is assumed to be all ones.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_get_closest_affine.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_get_closest_affine", *args, **kwargs)
