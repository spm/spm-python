from spm.__wrapper__ import Runtime


def spm_ovhelper_3Dreg(*args, **kwargs):
    """
      Helper function to register spm_orthviews plugins via spm_XYZreg  
        FORMAT spm_ovhelper_3Dreg('register', h, V)  
        Register a (3D) graphics with the main spm_orthviews display. This will  
        draw 3D crosshairs at the current spm_orthviews position and update  
        them whenever the spm_orthviews cursor moves.  
        h - a graphics handle or a tag of graphics handle to register  
        V - a volume handle (or equivalent) containing dimensions and  
            voxel-to-world mapping information  
         
        FORMAT spm_ovhelper_3Dreg('unregister', h)  
        h - a graphics handle or a tag of graphics handle to unregister  
         
        FORMAT spm_ovhelper_3Dreg('setcoords', xyz, h)  
        Update position of crosshairs in 3D display  
        xyz - new crosshair coordinates (in mm)  
        h - a graphics handle or a tag of graphics handle to update  
         
        FORMAT spm_ovhelper_3Dreg('xhairson', h)  
        FORMAT spm_ovhelper_3Dreg('xhairsoff', h)  
        Toggle display of crosshairs in 3D display.  
        h - a graphics handle or a tag of graphics handle   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_orthviews/spm_ovhelper_3Dreg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ovhelper_3Dreg", *args, **kwargs, nargout=0)
