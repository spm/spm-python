from spm.__wrapper__ import Runtime


def spm_coreg(*args, **kwargs):
    """
      Between modality coregistration using information theory  
        FORMAT x = spm_coreg(VG,VF,flags)  
        VG    - handle for reference image (see spm_vol).  
        VF    - handle for source (moved) image.  
        flags - a structure containing the following elements:  
                 sep      - optimisation sampling steps (mm)  
                            default: [4 2]  
                 params   - starting estimates (6 elements)  
                            default: [0 0 0  0 0 0]  
                 cost_fun - cost function string:  
                              'mi'  - Mutual Information  
                              'nmi' - Normalised Mutual Information  
                              'ecc' - Entropy Correlation Coefficient  
                              'ncc' - Normalised Cross Correlation  
                            default: 'nmi'  
                 tol      - tolerences for accuracy of each param  
                            default: [0.02 0.02 0.02 0.001 0.001 0.001]  
                 fwhm     - smoothing to apply to 256x256 joint histogram  
                            default: [7 7]  
                 graphics - display coregistration outputs  
                            default: ~spm('CmdLine')  
         
        x     - the parameters describing the rigid body rotation, such that a  
                mapping from voxels in G to voxels in F is attained by:  
                VF.mat\spm_matrix(x(:)')*VG.mat  
         
        At the end, the voxel-to-voxel affine transformation matrix is  
        displayed, along with the histograms for the images in the original  
        orientations, and the final orientations. The registered images are  
        displayed at the bottom.  
       __________________________________________________________________________  
         
        The registration method used here is based on the work described in:  
        A Collignon, F Maes, D Delaere, D Vandermeulen, P Suetens & G Marchal  
        (1995) "Automated Multi-modality Image Registration Based On  
        Information Theory". In the proceedings of Information Processing in  
        Medical Imaging (1995).  Y. Bizais et al. (eds.).  Kluwer Academic  
        Publishers.  
         
        The original interpolation method described in this paper has been  
        changed in order to give a smoother cost function.  The images are  
        also smoothed slightly, as is the histogram.  This is all in order to  
        make the cost function as smooth as possible, to give faster convergence  
        and less chance of local minima.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_coreg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_coreg", *args, **kwargs)
