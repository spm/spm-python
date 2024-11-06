from spm.__wrapper__ import Runtime


def spm_mip_ui(*args, **kwargs):
    """
      GUI for displaying MIPs with interactive pointers  
        FORMAT hMIPax = spm_mip_ui(Z,XYZ,M,DIM,F,units)  
        Z       - {1 x ?} vector point list of SPM values for MIP  
        XYZ     - {3 x ?} matrix of coordinates of points (Talairach coordinates)  
        M       - voxels - > mm matrix  
        DIM     - image dimensions {voxels}  
        F       - Figure (or axes) to work in [Defaults to gcf]  
        hMIPax  - handle of MIP axes  
        units   - units of space  
         
        FORMAT xyz = spm_mip_ui('GetCoords',h)  
        h       - Handle of MIP axes, or figure containing MIP axis [default gcf]  
        xyz     - Current Talairach coordinates of cursor  
         
        FORMAT [xyz,d] = spm_mip_ui('SetCoords',xyz,h,hC)  
        xyz     - (Input) {3 x 1} vector of desired Talairach coordinates  
        h       - Handle of MIP axes, or figure containing MIP axis [default gcf]  
        hC      - Handle of calling object, if used as a callback. [Default 0]  
        xyz     - (Output) {3 x 1} vector of voxel centre nearest desired xyz co-ords  
        d       - Euclidean distance from desired co-ords & nearest voxel  
       __________________________________________________________________________  
         
        spm_mip_ui displays a maximum intensity projection (using spm_mip)  
        with draggable cursors.  
         
        See spm_mip.m for details of MIP construction, display, and the brain  
        outlines used.  
                                  ----------------  
         
        The cursor can be dragged to new locations in three ways:  
         
        (1) Point & drop: Using the primary "select" mouse button, click on a  
            cursor and drag the crosshair which appears to the desired location.  
            On dropping, the cursors jump to the voxel centre nearest the drop  
            site.  
         
        (2) Dynamic drag & drop: Using the middle "extend" mouse button, click on  
            a cursor and drag it about. The cursor follows the mouse, jumping to  
            the voxel centre nearest the pointer. A dynamically updating  
            information line appears above the MIP and gives the current  
            coordinates. If the current voxel centre is in the XYZ pointlist,  
            then the corresponding image value is also printed.  
         
        (3) Magnetic drag & drop: As with "Dynamic drag & drop", except the cursors  
            jump to the voxel centre in the pointlist nearest to the cursor. Use  
            the right "alt" mouse button for "magnetic drag & drop".  
         
        In addition a ContextMenu is provided, giving the option to jump the  
        cursors to the nearest suprathreshold voxel, the nearest local  
        maximum, or to the global maximum. (Right click on the MIP to bring up  
        the ContextMenu.) A message in the MATLAB command window describes the  
        jump.  
         
                                  ----------------  
         
        The current cursor position (constrained to lie on a voxel) can be  
        obtained by xyz=spm_mip_ui('GetCoords',hMIPax), and set with  
        xyz=spm_mip_ui('SetCoords',xyz,hMIPax), where hMIPax is the handle of  
        the MIP axes, or of the figure containing a single MIP [default gcf].  
        The latter rounds xyz to the nearest voxel center, returning the  
        result.  
         
        spm_mip_ui handles all the callbacks required for moving the cursors, and  
        is "registry" enabled (See spm_XYZreg.m). Programmers help is below in the  
        main body of the function.  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mip_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mip_ui", *args, **kwargs)
