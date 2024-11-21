from spm.__wrapper__ import Runtime


def spm_image(*args, **kwargs):
    """
      Image and header display  
        FORMAT spm_image  
        FORMAT spm_image('Display',fname)  
       __________________________________________________________________________  
         
        spm_image is an interactive facility that allows orthogonal sections from  
        an image volume to be displayed.  Clicking the cursor on either of the  
        three images moves the point around which the orthogonal sections are  
        viewed.  The coordinates of the cursor are shown both in voxel  
        coordinates and millimeters within some fixed framework. The intensity  
        at that point in the image (sampled using the current interpolation  
        scheme) is also given. The position of the crosshairs can also be moved  
        by specifying the coordinates in millimeters to which they should be  
        moved.  Clicking on the 'Origin' button will move the cursor back to the  
        origin  (analogous to setting the crosshair position (in mm) to [0 0 0]).  
         
        The images can be re-oriented by entering appropriate translations,  
        rotations and zooms into the panel on the left.  The transformations can  
        then be saved by hitting the 'Reorient...' button.  The transformations  
        that were applied to the image are saved to the header information of the  
        selected images.  The transformations are considered to be relative to  
        any existing transformations that may be stored. Note that the order that  
        the transformations are applied in is the same as in spm_matrix.m.  
        Clicking on the 'Set Origin' button will apply the appropriate  
        translation to the image such that the origin ([0 0 0] (in mm)) will be  
        set to the current location of the crosshair.  To save the transformation  
        you need to click the 'Reorient...' button.   
         
        The right panel shows miscellaneous information about the image.  
        This includes:  
          Dimensions - the x, y and z dimensions of the image.  
          Datatype   - the computer representation of each voxel.  
          Intensity  - scalefactors and possibly a DC offset.  
          Miscellaneous other information about the image.  
          Vox size   - the distance (in mm) between the centres of  
                       neighbouring voxels.  
          Origin     - the voxel at the origin of the coordinate system  
          Dir Cos    - Direction cosines.  This is a widely used representation  
                       of the orientation of an image.  
         
        There are also a few options for different resampling modes, zooms etc.  
        You can also flip between voxel space or world space.  If you are  
        re-orienting the images, make sure that world space is specified. SPM{.}  
        or images can be superimposed and the intensity windowing can also be  
        changed.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_image.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_image", *args, **kwargs, nargout=0)
