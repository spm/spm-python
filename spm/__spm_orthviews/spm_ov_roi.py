from spm.__wrapper__ import Runtime


def spm_ov_roi(*args, **kwargs):
    """
      ROI tool - plugin for spm_orthviews  
         
        With ROI tool it is possible to create new or modify existing mask images  
        interactively. ROI tool can be launched via the spm_orthviews image  
        context menu.  
        While ROI tool is active, mouse buttons have the following functions:  
        left       Reposition crosshairs  
        middle     Perform ROI tool box selection according to selected edit mode at  
                   crosshair position  
        right      context menu  
          
        Menu options and prompts explained:  
        Launch     Initialise ROI tool in current image  
                   'Load existing ROI image? (yes/no)'   
                     If you want to modify an existing mask image (e.g. mask.img from  
                     a fMRI analysis), press 'yes'. You will then be prompted to  
                   'Select ROI image'  
                     This is the image that will be loaded as initial ROI.  
                     If you want to create a new ROI image, you will first be  
                     prompted to  
                   'Select image defining ROI space'  
                     The image dimensions, voxel sizes and slice orientation will  
                     be read from this image. Thus you can edit a ROI based on a  
                     image with a resolution and slice orientation different from  
                     the underlying displayed image.  
         
        Once ROI tool is active, the menu consists of three parts: settings,  
        edit operations and load/save operations.  
        Settings  
        --------  
        Selection  Operation performed when pressing the middle mouse button or  
        mode       by clustering operations.  
                   'Set selection'  
                     The selection made with the following commands will  
                     be included in your ROI.  
                   'Clear selection'   
                     The selection made with the following commands will  
                     be excluded from your ROI.  
        Box size   Set size of box to be (de)selected when pressing the  
                   middle mouse button.  
        Polygon    Set number of adjacent slices selected by one polygon  
        slices     drawing.   
        Cluster    Set minimum cluster size for "Cleanup clusters" and  
        size       "Connected cluster" operations.  
        Erosion/   During erosion/dilation operations, the binary mask will be  
        dilation   smoothed. At boundaries, this will result in mask values   
        threshold  that are not exactly zero or one, but somewhere in  
                   between. Whether a mask will be eroded (i.e. be smaller than  
                   the original) or dilated (i.e. grow) depends on this  
                   threshold. A threshold below 0.5 dilates, above 0.5 erodes a  
                   mask.   
        Edit actions  
        ------------  
        Polygon    Draw an outline on one of the 3 section images. Voxels  
                   within the outline will be added to the ROI. The same  
                   outline can be applied to a user-defined number of  
                   consecutive slices around the current crosshair position.  
        Threshold  You will be prompted to enter a [min max] threshold. Only  
                   those voxels in the ROI image where the intensities of the  
                   underlying image are within the [min max] range will survive  
                   this operation.  
        Connected  Select only voxels that are connected to the voxel at  
        cluster    current crosshair position through the ROI.  
        Cleanup    Keep only clusters that are larger than a specified cluster   
        clusters   size.  
        Erode/     Erode or dilate a mask, using the current erosion/dilation  
        Dilate     threshold.  
        Invert     Invert currently defined ROI  
        Clear      Clear ROI, but keep ROI space information  
        Add ROI from file(s)  
                   Add ROIs from file(s) into current ROI set. According to the  
                   current edit mode voxels unequal zero will be set or  
                   cleared. The image files will be resampled and thus do not  
                   need to have the same orientation or voxel size as the  
                   original ROI.  
        Save actions  
        ------------  
        Save       Save ROI image  
        Save As    Save ROI image under a new file name  
                   The images will be rescaled to 0 (out of mask) and 1 (in  
                   mask).  
        Quit       Quit ROI tool  
         
        This routine is a plugin to spm_orthviews. For general help about  
        spm_orthviews and plugins type  
                    help spm_orthviews  
        at the MATLAB prompt.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_orthviews/spm_ov_roi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ov_roi", *args, **kwargs)
