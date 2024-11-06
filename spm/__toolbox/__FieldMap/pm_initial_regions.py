from spm.__wrapper__ import Runtime


def pm_initial_regions(*args, **kwargs):
    """
      Divides 2 or 3D phasemap (pm) into nstep equally wide  
        angle ranges and returns the connected components  
        of those.  
        FORMAT [irima,cn] = pm_initial_regions(pm,mask,nstep)  
         
        Input  
        pm      : Non-unwrapped phase-map.  
        mask    : Tells us what regions of pm to consider.  
        nstep   : Defines the number of equi-wide angle ranges  
                  between -pi and pi that we should use.  
                  If linear phase-ramps have been removed from  
                  the data we may have values outside the  
                  -pi->pi range. We will then simply divide  
                  the observed range into nstep steps.  
         
        Output:  
        irima   : Image with connected regions of phase-values  
                  within each range.  
        cn      : Total number of conncted regions.  
         
        This routine is used to make the initial division into  
        a set of regions, which within each it is very unlikely that  
        a phase-wrap has occurred, that is the preamble for Mark  
        J's method. A higher value for nstep makes it less likely  
        that a wrap is included within a region, but will also  
        lead to more regions->longer execution time.  
         
        N.B. The interval > phi <= is based on the observation that  
        angle(-1) returns pi (rather than -pi).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_initial_regions.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pm_initial_regions", *args, **kwargs)
