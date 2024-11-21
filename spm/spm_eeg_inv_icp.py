from spm.__wrapper__ import Runtime


def spm_eeg_inv_icp(*args, **kwargs):
    """
      Iterative Closest Point (ICP) registration algorithm  
        Surface matching computation: registration from one 3D surface onto  
        another 3D surface.  
         
        FORMAT [M1] = spm_eeg_inv_icp(data1,data2,[fid1],[fid2],[Fmri],[Fhsp],[aff])  
        Input:  
        data1      - locations of the first set of points corresponding to the  
                     3D surface to register onto [3 x n]  
        data2      - locations of the second set of points corresponding to the  
                     second 3D surface to be registered [3 x p]  
        fid1       - sMRI fiducials [default: []]  
        fid2       - sens fiducials [default: []]  
        Fmri       - graphics handle for sMRI points [default: none]  
        Fhsp       - graphics handle for headshape [default: none]  
        aff        - flag for 12-parameter affine transform [default: 0]  
         
        Output:  
        M1         - 4 x 4 affine transformation matrix for sensor space  
         
        Landmarks (fiducials) based registration  
        Fiducial coordinates must be given in the same order in both files  
         
       --------------------------------------------------------------------------  
        Adapted from code available at http://www.csse.uwa.edu.au/~ajmal/code/icp.m  
        written by Ajmal Saeed Mian {ajmal@csse.uwa.edu.au}, Computer Science,   
        The University of Western Australia. The code may be used, modified and   
        distributed for research purposes with acknowledgement of the author and   
        inclusion this copyright information.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_icp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_icp", *args, **kwargs)
