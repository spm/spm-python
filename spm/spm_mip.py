from spm.__wrapper__ import Runtime


def spm_mip(*args, **kwargs):
    """
      SPM Maximum Intensity Projection  
        FORMAT mip = spm_mip(Z,XYZ,M,units)  
        Z       - vector point list of SPM values for MIP  
        XYZ     - matrix of coordinates of points (mip coordinates)  
        M       - voxels - > mip matrix or size of voxels (mm)  
        units   - defining space     [default {'mm' 'mm' 'mm'}]  
         
        mip     - maximum intensity projection  
                  if no output, the mip is displayed in current figure.  
       __________________________________________________________________________  
         
        If the data are 2 dimensional [DIM(3) = 1] the projection is simply an  
        image, otherwise:  
         
        spm_mip creates and displays a maximum intensity projection of a point  
        list of voxel values (Z) and their location (XYZ) in three orthogonal  
        views of the brain. It is assumed voxel locations conform to the space  
        defined in the atlas of Talairach and Tournoux (1988); unless the third  
        dimension is time.  
         
        This routine loads a mip outline from MIP.mat. This is an image with  
        contours and grids defining the space of Talairach & Tournoux (1988).  
        mip95 corresponds to the Talairach atlas, mip96 to the MNI templates.  
        The outline and grid are superimposed at intensity 0.4.  
         
        A customised mip outline can be used instead of the default.  
         
        A default colormap of 64 levels is assumed. The pointlist image is  
        scaled to fit in the interval [1/9,1]*64 for display. Flat images  
        are scaled to 1*64.  
         
        If M is not specified, it is assumed the XYZ locations are   
        in Talairach mm.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mip.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mip", *args, **kwargs)
