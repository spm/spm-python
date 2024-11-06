from spm.__wrapper__ import Runtime


def spm_mesh_pack_points(*args, **kwargs):
    """
      Place approximately equally spaced points over a convex (ideally) mesh  
        FORMAT [Pout,ms2s ,ims2s,n] = spm_mesh_pack_points(S)  
          S          - input structure  
        Fields of S:  
          S.g        - gifti mesh                  - Default: mni scalp template  
          S.niter    - number of iterations        - Default: 2000  
          S.p        - initial points (nx3 matrix) - Default: guesses...  
          S.space    - desired spacing (mm)        - Default: 10  
          S.division - number of mesh subdivisions - Default: 3  
          S.nDens    - number of density checks    - Default: 40  
        Output:  
          Pnew        - N x 3 matrix containing new points  
          ms2s        - nearest neighbour distances  
          ims2s       - initial nearest neighbour distances  
          n           - number of sensors at each iteration  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_mesh_pack_points.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_pack_points", *args, **kwargs)
