from spm.__wrapper__ import Runtime


def spm_mesh_render(*args, **kwargs):
    """
      Display a surface mesh & various utilities  
        FORMAT H = spm_mesh_render('Disp',M,'PropertyName',propertyvalue)  
        M        - a GIfTI filename/object or patch structure  
        H        - structure containing handles of various objects  
        Opens a new figure unless a 'parent' Property is provided with an axis  
        handle.  
         
        FORMAT H = spm_mesh_render(M)  
        Shortcut to previous call format.  
         
        FORMAT H = spm_mesh_render('ContextMenu',AX)  
        AX       - axis handle or structure returned by spm_mesh_render('Disp',...)  
         
        FORMAT H = spm_mesh_render('Overlay',AX,P)  
        AX       - axis handle or structure given by spm_mesh_render('Disp',...)  
        P        - data to be overlaid on mesh (see spm_mesh_project)  
         
        FORMAT H = spm_mesh_render('ColourBar',AX,MODE)  
        AX       - axis handle or structure returned by spm_mesh_render('Disp',...)  
        MODE     - {['on'],'off'}  
         
        FORMAT H = spm_mesh_render('ColourMap',AX,MAP)  
        AX       - axis handle or structure returned by spm_mesh_render('Disp',...)  
        MAP      - a colour map matrix  
         
        FORMAT MAP = spm_mesh_render('ColourMap',AX)  
        Retrieves the current colourmap.  
         
        FORMAT H = spm_mesh_render('View',AX, V)  
        AX       - axis handle or structure returned by spm_mesh_render('Disp',...)  
        V        - viewpoint specification (see view())  
         
        FORMAT spm_mesh_render('Register',AX,hReg)  
        AX       - axis handle or structure returned by spm_mesh_render('Disp',...)  
        hReg     - Handle of HandleGraphics object to build registry in.  
        See spm_XYZreg for more information.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_render.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_render", *args, **kwargs)
