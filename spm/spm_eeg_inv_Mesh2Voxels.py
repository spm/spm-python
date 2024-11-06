from spm.__wrapper__ import Runtime


def spm_eeg_inv_Mesh2Voxels(*args, **kwargs):
    """
      Convert a mesh representation of M/EEG power into a smoothed image  
        FORMAT [D] = spm_eeg_inv_Mesh2Voxels(D,[val])  
        Input:  
        D        - MEEG object or filename of M/EEG mat-file (optional)  
         
            D.inv{val}.contrast.display:   display image at the end {true, [false]}  
            D.inv{val}.contrast.space:     native [0] or MNI {1} output space  
            D.inv{val}.contrast.format:    output file format {['image'], 'mesh'}  
            D.inv{val}.contrast.smoothing: # iterations for cortical smoothing  
         
        Output:  
        D        - MEEG object containing the new image filenames in fields:  
         
            D.inv{val}.contrast.fname  
       __________________________________________________________________________  
         
        Non-linear interpolation of a Mesh contrast into MNI Voxel space  
        This routine is used to produce a 3D image canonical sMRI  
        space (in voxel coordinates) from a cortical mesh (3D surface).  
        This yields a NIfTI image of the summary statistics of the cortical  
        activity for the effect of interest. This image can then enter the  
        classical SPM routines for statistical testing.  
        The [non-negative] mean square contrast is smoothed both on the mesh  
        (using a graph Laplacian) and then in voxel-space using a conventional  
        Gaussian filter.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_Mesh2Voxels.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_Mesh2Voxels", *args, **kwargs)
