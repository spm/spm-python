from spm._runtime import Runtime


def _mkfilt_eloreta(*args, **kwargs):
    """
      makes spatial filter according to eLoreta   
        usage  A=mkfilt_eloreta(L); or  A=mkfilt_eloreta(L,regu);  
         
        input L:  NxMxP leadfield tensor for N channels, M voxels, and   
                  P dipole directions. Typically P=3. (If you do MEG for   
                  a spherical volume conductor or reduce the rank, you must   
                  reduce L such that it has full rank for each voxel, such that,  
                  e.g., P=2)  
              regu: optional regularization parameter (default is .05 corresponding   
                    to 5% of the average of the eigenvalues of some matrix to be inverted.)   
          
        output A: NxMxP tensor of spatial filters. If x is the Nx1 data vector at time t.   
                  then A(:,m,p)'*x is the source activity at time t in voxel m in source direction  
                  p.   
          
        code implemented by Guido Nolte  
        please cite  
        R.D. Pascual-Marqui: Discrete, 3D distributed, linear imaging methods of electric neuronal activity. Part 1: exact, zero  
        error localization. arXiv:0710.3341 [math-ph], 2007-October-17, http://arxiv.org/pdf/0710.3341   
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/mkfilt_eloreta.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mkfilt_eloreta", *args, **kwargs)
