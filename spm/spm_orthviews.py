from spm.__wrapper__ import Runtime


def spm_orthviews(*args, **kwargs):
    """
      Display orthogonal views of a set of images  
        FORMAT H = spm_orthviews('Image',filename[,area[,F]])  
        filename - name of image to display  
        area     - position of image {relative}  
                   [left, bottom, width, height]  
        F        - figure handle  
        H        - handle for orthogonal sections  
         
        FORMAT spm_orthviews('Reposition',centre)  
        centre   - X, Y & Z coordinates of centre voxel {mm}  
         
        FORMAT spm_orthviews('Space'[,handle[,M,dim]])  
        handle   - the view to define the space by, optionally with extra  
                   transformation matrix and dimensions (e.g. one of the blobs  
                   of a view)  
        with no arguments - puts things into mm space  
         
        FORMAT H = spm_orthviews('Caption', handle, string, [Property, Value])  
        handle   - the view to which a caption should be added  
        string   - the caption text to add  
        Property,Value - optional, e.g. 'FontWeight', 'Bold'  
        H        - the handle to the object whose String property has the caption  
         
        FORMAT spm_orthviews('BB',bb)  
        bb       - bounding box  
                   [loX loY loZ  
                    hiX hiY hiZ]  
         
        FORMAT spm_orthviews('MaxBB')  
        Set the bounding box big enough to display the whole of all images.  
         
        FORMAT spm_orthviews('Resolution'[,res])  
        res      - resolution (mm)  
        Set the sampling resolution for all images. The effective resolution will  
        be the minimum of res and the voxel sizes of all images. If no resolution  
        is specified, the minimum of 1mm and the voxel sizes of the images is  
        used.  
         
        FORMAT spm_orthviews('Zoom'[,fov[,res]])  
        fov      - half width of field of view (mm)  
        res      - resolution (mm)  
        Set the displayed part and sampling resolution for all images. The image  
        display will be centered at the current crosshair position. The image  
        region [xhairs-fov xhairs+fov] will be shown.  
        If no argument is given or fov == Inf, the image display will be reset to  
        "Full Volume". If fov == 0, the image will be zoomed to the bounding box  
        from spm_get_bbox for the non-zero voxels of the image. If fov is NaN,  
        then a threshold can be entered, and spm_get_bbox will be used to derive  
        the bounding box of the voxels above this threshold.  
        Optionally, the display resolution can be set as well.  
         
        FORMAT spm_orthviews('Redraw')  
        Redraw the images.  
         
        FORMAT spm_orthviews('Reload_mats')  
        Reload the voxel-world mapping matrices from the headers stored on disk,  
        e.g. following reorientation of some images.  
         
        FORMAT spm_orthviews('Delete', handle)  
        handle   - image number to delete  
         
        FORMAT spm_orthviews('Reset')  
        Clear the orthogonal views  
         
        FORMAT spm_orthviews('Pos')  
        Return the coordinate of the crosshairs in millimetres in the standard  
        space.  
         
        FORMAT spm_orthviews('Pos', i)  
        Return the voxel coordinate of the crosshairs in the image in the ith  
        orthogonal section.  
         
        FORMAT spm_orthviews('Xhairs','off') OR spm_orthviews('Xhairs')  
        Disable the cross-hairs on the display.  
         
        FORMAT spm_orthviews('Xhairs','on')  
        Enable the cross-hairs.  
         
        FORMAT spm_orthviews('Interp',hld)  
        Set the hold value to hld (see spm_slice_vol).  
         
        FORMAT spm_orthviews('AddBlobs',handle,XYZ,Z,mat,name)  
        Add blobs from a pointlist to the image specified by the handle(s).  
        handle   - image number to add blobs to  
        XYZ      - blob voxel locations  
        Z        - blob voxel intensities  
        mat      - matrix from voxels to millimetres of blob  
        name     - a name for this blob  
        This method only adds one set of blobs, and displays them using a split  
        colour table.  
         
        FORMAT spm_orthviews('SetBlobsMax', vn, bn, mx)  
        Set maximum value for blobs overlay number bn of view number vn to mx.  
         
        FORMAT spm_orthviews('AddColouredBlobs',handle,XYZ,Z,mat,colour,name)  
        Add blobs from a pointlist to the image specified by the handle(s)  
        handle   - image number to add blobs to  
        XYZ      - blob voxel locations  
        Z        - blob voxel intensities  
        mat      - matrix from voxels to millimeters of blob.  
        colour   - the 3 vector containing the colour that the blobs should be  
        name     - a name for this blob  
        Several sets of blobs can be added in this way, and it uses full colour.  
        Although it may not be particularly attractive on the screen, the colour  
        blobs print well.  
         
        FORMAT spm_orthviews('AddColourBar',handle,blobno)  
        Add colourbar for a specified blob set.  
        handle    - image number  
        blobno    - blob number  
         
        FORMAT spm_orthviews('RemoveBlobs',handle)  
        Remove all blobs from the image specified by the handle(s).  
         
        FORMAT spm_orthviews('Addtruecolourimage',handle,filename,colourmap,prop,mx,mn)  
        Add blobs from an image in true colour.  
        handle    - image number to add blobs to [Default: 1]  
        filename  - image containing blob data [Default: GUI input]  
        colourmap - colormap to display blobs in [Default: GUI input]  
        prop      - intensity proportion of activation cf grayscale [default: 0.4]  
        mx        - maximum intensity to scale to [maximum value in activation image]  
        mn        - minimum intensity to scale to [minimum value in activation image]  
         
        FORMAT spm_orthviews('Register',hReg)  
        hReg      - Handle of HandleGraphics object to build registry in  
        See spm_XYZreg for more information.  
         
        FORMAT spm_orthviews('AddContext',handle)  
        FORMAT spm_orthviews('RemoveContext',handle)  
        handle    - image number to add/remove context menu to  
         
        FORMAT spm_orthviews('ZoomMenu',zoom,res)  
        FORMAT [zoom, res] = spm_orthviews('ZoomMenu')  
        zoom      - A list of predefined zoom values  
        res       - A list of predefined resolutions  
        This list is used by spm_image and spm_orthviews('addcontext',...) to  
        create the 'Zoom' menu. The values can be retrieved by calling  
        spm_orthviews('ZoomMenu') with 2 output arguments. Values of 0, NaN and  
        Inf are treated specially, see the help for spm_orthviews('Zoom' ...).  
       __________________________________________________________________________  
         
        PLUGINS  
        The display capabilities of spm_orthviews can be extended with plugins.  
        These are located in the spm_orthviews subdirectory of the SPM  
        distribution.  
        The functionality of plugins can be accessed via calls to  
        spm_orthviews('plugin_name', plugin_arguments). For detailed descriptions  
        of each plugin see help spm_orthviews/spm_ov_'plugin_name'.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_orthviews.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_orthviews", *args, **kwargs)
