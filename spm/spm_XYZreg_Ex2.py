from spm.__wrapper__ import Runtime


def spm_XYZreg_Ex2(*args, **kwargs):
    """
      Example of Registry enabled XYZ GUI control / function  
        FORMAT...  
       _______________________________________________________________________  
         
        Help goes here...  
         
        Object must be indentifiable via a unique HandleGraphics object.  
        In this code, this handle is called hMe.  
         
        This HandleGraphics objects 'UserData' *must* be a structure.  
        The structure must have a field called 'hReg', which stores the handle  
        of the registry when linked, and is empty when not. Some utility features  
        of spm_XYZreg will set/delete the handle directly...  
         
        There must be a 'SetCoords' function for this object, with call:  
          spm_res_ui('SetCoords',xyz,hMe,hC)  
        ...this can handle interna, coordinate setting (as in this example), but  
        must also call the registry.  
         
        The registry update function is:  
          spm_XYZreg('SetCoords',xyz,hReg,hMe);  
        ...which must be called at all points where the local coordinates can be  
        changed. It is robust to invalid or empty hReg.  
         
        It's *vital* to specify caller handles (hC), so that the registry doesn't  
        end up in an infinite loop of updating!  
         
        Hey, if your function has multiple places where you can change the XYZ,  
        you could use an ``internal'' registry locally, with the external registry  
        as one of it's entries! (I think?)  
         
       _______________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_XYZreg_Ex2.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_XYZreg_Ex2", *args, **kwargs)
