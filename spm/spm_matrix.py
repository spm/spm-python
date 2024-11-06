from spm.__wrapper__ import Runtime


def spm_matrix(*args, **kwargs):
    """
      Return an affine transformation matrix  
        FORMAT [A] = spm_matrix(P [,order])  
        P(1)  - x translation  
        P(2)  - y translation  
        P(3)  - z translation  
        P(4)  - x rotation about - {pitch} (radians)  
        P(5)  - y rotation about - {roll}  (radians)  
        P(6)  - z rotation about - {yaw}   (radians)  
        P(7)  - x scaling  
        P(8)  - y scaling  
        P(9)  - z scaling  
        P(10) - x affine  
        P(11) - y affine  
        P(12) - z affine  
         
        order - application order of transformations [Default: 'T*R*Z*S']  
         
        A     - affine transformation matrix  
       __________________________________________________________________________  
         
        spm_matrix returns a matrix defining an orthogonal linear (translation,  
        rotation, scaling or affine) transformation given a vector of  
        parameters (P).  By default, the transformations are applied in the  
        following order (i.e., the opposite to which they are specified):  
         
        1) shear  
        2) scale (zoom)  
        3) rotation - yaw, roll & pitch  
        4) translation  
         
        This order can be changed by calling spm_matrix with a string as a  
        second argument. This string may contain any valid MATLAB expression  
        that returns a 4x4 matrix after evaluation. The special characters 'S',  
        'Z', 'R', 'T' can be used to reference the transformations 1)-4)  
        above. The default order is 'T*R*Z*S', as described above.  
         
        SPM uses a PRE-multiplication format i.e. Y = A*X where X and Y are 4 x n  
        matrices of n coordinates.  
       __________________________________________________________________________  
         
        See also: spm_imatrix.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_matrix.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_matrix", *args, **kwargs)
