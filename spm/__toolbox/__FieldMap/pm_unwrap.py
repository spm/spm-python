from spm.__wrapper__ import Runtime


def pm_unwrap(*args, **kwargs):
    """
      Unwrapping of phasemap  
        When measuring phase one cannot easily distinguish between e.g. a phase  
        of 182 degrees, and one of -178 degrees. One tries to distinguish these  
        cases by using neighbourhood information. So in the example above, if we  
        find that a neighbouring voxel has a phase of 150 degres it seems much  
        more likely that the "true" phase is 182 degrees than -178 degrees. It's  
        trickier than it sounds.  
        FORMAT: [upm,(angvar),(mask),(opm)] = pm_unwrap(ci,pxs,method)  
        or  
        FORMAT: [upm,(angvar),(mask),(opm)] = pm_unwrap(ci,pxs)  
        or  
        FORMAT: [upm,(angvar),(mask),(opm)] = pm_unwrap(P,method)  
        or  
        FORMAT: [upm,(angvar),(mask),(opm)] = pm_unwrap(P)  
         
        Input:  
        ci          : Complex image volume corresponding  
                      to  abs(te2).*exp(i*angle(te2))./exp(i*angle(te1));  
                      where te1 and te2 corresponds to the complex  
                      images obtained with the short and the long  
                      echo-time respectively, and i denotes sqrt(-1).  
        pxs         : 3x1 (or 2x1) array with pixel sizes.  
         
        or  
         
        P           : File structure (from) spm_vol, containing complex  
                      image volume as per above.  
         
        method      : Determines which method should be used  
                      for phase-unwrapping. The options are  
                      'Huttonish', 'Mark2D', 'Mark3D' and 'hybrid'.  
        'Huttonish' : Loosely (hence -ish) based on method described  
                      in Hutton et al. Gets an estimate of the  
                      uncertainty of the phase angle at each point  
                      and unwraps in a "watershed" fashion from  
                      a high certainty seed towards more uncertain  
                      areas.  
        'Mark2D'    : Method suggested for high-res data in  
                      Jenkinssons MRM paper.  
        'Mark3D'    : Method suggested for low-res data in  
                      Jenkinssons MRM paper.  
         
        Output:  
        upm         : Phasemap (corresponding to angle(ci))  
                      after unwrapping of phase jumps.  
        angvar      : Map of the variance of the phase-angle  
                      estimates. This is used internally to  
                      guide the unwrapping procedure, and  
                      can also be used if one whishes to  
                      do a weighted fitting of some smooth  
                      basis set to the unwrapped phasemap.  
        mask        : Binary mask indicating what voxels  
                      have been unwrapped.  
        opm         : angle(ci)  
         
        Light reading:  
         
        Examples of water-shed/flood-fill based unwrapping  
        algorithms:  
         
        Hutton C, Bork A, Josephs O, Deichmann R, Ashburner J,  
        Turner R. 2002. Image distortion correction in fMRI: A  
        quantitative evaluation. NeuroImage 16:217-240.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_unwrap.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pm_unwrap", *args, **kwargs)
