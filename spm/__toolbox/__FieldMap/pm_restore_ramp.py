from spm.__wrapper__ import Runtime


def pm_restore_ramp(*args, **kwargs):
    """
       
        Restores linear phase-ramps in the x-, y- and z-direction  
        that has previously been removed from pm by pm_estimate_ramp.  
        FORMAT: pm = pm_estimate_ramp(pm,mask,ramps)  
         
        Input:  
        pm     : 2 or 3D phasemap that has been unwrapped and  
                 that has had its ramps removed by pm_remove_ramp  
        mask   : Mask that indicates which voxels are worth  
                 bothering with and which are not.  
        ramps  : 3x1 vector signifying the slope of the ramps in  
                 the x-, y- and z-directions. This SHOULD be the  
                 values returned by a previous call to pm_estimate_ramp.  
         
        Output:  
        pm     : Same as pm in, but with linear ramps restored.  
         
        This routine was written on the suggestion of Mark J, and will  
        potentially improve performance of subsequent phase-unwrapping.  
        I haven't actually found it particularly helpful, and it may  
        simply have been a sneaky fMRIB attempt to delay the SPM  
        phasemap toolbox.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_restore_ramp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pm_restore_ramp", *args, **kwargs)
