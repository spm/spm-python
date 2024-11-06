from spm.__wrapper__ import Runtime


def pm_invert_phasemap(*args, **kwargs):
    """
      Inverting phasemaps (trickier than it sounds).  
        FORMAT ipm = invert_phasemap(pm)  
        or  
        FORMAT ipm = invert_phasemap(pm,idim)  
        or  
        FORMAT ipm = invert_phasemap(P)  
        or  
        FORMAT ipm = invert_phasemap(P,idim)  
        or  
        FORMAT invert_phasemap(P,fname)  
        or  
        FORMAT invert_phasemap(P,fname,idim)  
         
        Input:  
        pm      1, 2 or 3D array representing a displacement field that  
                is to be inverted along one direction.  
        idim    The dimension along which field is to be inverted.  
        P       File-struct or -name containing displacement field.  
        fname   Name of output file.  
         
        Output:  
        ipm     Displacement-field inverted along requested direction.  
         
        This is a gateway function to invert_phasemap_dtj (do the job)  
        which is a mex-file. The job of this routine is to handle some of  
        the basic book-keeping regarding format and file creation.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_invert_phasemap.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pm_invert_phasemap", *args, **kwargs)
