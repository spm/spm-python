from spm.__wrapper__ import Runtime


def spm_ROI(*args, **kwargs):
    """
      Region of Interest specification  
        FORMAT xY = spm_ROI(xY)  
        xY     - VOI structure  
           xY.def      - VOI definition [sphere, box, mask, cluster, all]  
           xY.rej      - cell array of disabled VOI definition options  
           xY.xyz      - centre of VOI {mm}  
           xY.spec     - VOI definition parameters  
           xY.str      - description of the VOI  
         
        FORMAT [xY, XYZmm, j] = spm_ROI(xY, XYZmm)  
        XYZmm  - [3xm] locations of voxels {mm}  
                 If an image filename, an spm_vol structure or a NIfTI object is  
                 given instead, XYZmm will be initialised to all voxels within  
                 the field of view of that image.  
         
        XYZmm  - [3xn] filtered locations of voxels {mm} (m>=n) within VOI xY  
        j      - [1xn] indices of input locations XYZmm within VOI xY  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ROI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ROI", *args, **kwargs)
