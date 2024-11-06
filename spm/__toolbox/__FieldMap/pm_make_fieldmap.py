from spm.__wrapper__ import Runtime


def pm_make_fieldmap(*args, **kwargs):
    """
      This function creates an unwrapped fieldmap (in Hz) from either  
        a single or double echo complex image volume. In the case of a  
        "single-echo" image, that will have been created by the vendor  
        sequence out of two acquisitions with different echo times.  
        The complex image volume(s) may consist of either real and  
        imaginary OR phase and magnitude components  
         
        FORMAT fm = pm_make_fieldmap(P,flags);  
         
        Input:  
        P           : A matrix of 2 or 4 filenames, or  
                      a struct array of 2 or 4 memory mapped image volumes.  
        flags       : Struct containing parameters guiding the unwrapping.  
        .iformat    : 'RI' or 'PM'  
                      'RI' - input images are Real and Imaginary. (default)  
                      'PM' - input images are Phase and Magnitude  
        .method     : 'Huttonish', 'Mark3D' or 'Mark2D'  
                      'Huttonish': Flood-fill based unwrapping progressing  
                       from low to high uncertainty areas.  
                      'Mark3D': Region-merging based method merging 3D  
                       regions starting with the big ones. (default)  
                      'Mark2D': Region-merging based method merging  
                       slicewise 2D regions until all connected regions  
                       within slices have been merged before moving on  
                       to merging the slices.  
        .fwhm       : FWHM (mm) of Gaussian filter used to implement  
                      a weighted (with the reciprocal of the angular  
                      uncertainty) smoothing of the unwrapped maps.  
                      (default: 10mm)  
        .pad        : Size (in-plane voxels) of padding kernel. This  
                      is an option to replace non-unwrapped voxels  
                      (i.e. those that have been considered to noisy)  
                      with an average of neighbouring unwrapped voxels.  
                      The size defines the size of the neighbourhood.  
                      (default = 0);  
        .etd        : Echo time difference (ms).(default = 10)  
        .ws         : Weighted or unweighted smoothing (default = 1)  
        .bmask      : Brain mask  
         
        Output:  
        fm          : Structure containing fieldmap information  
        The elements of the fm structure are:  
          fm.upm    : unwrapped fieldmap in Hz  
          fm.mask   : binary image used to mask fieldmap  
          fm.opm    : phase map in radians  
          fm.jac    : Jacobian of the fieldmap  
       _______________________________________________________________________  
         
            .iformat = 'RI'  (this the default mode if not specified)  
         
        P(1)        : real part of complex fieldmap image  
        P(2)        : imaginary part of complex fieldmap image  
              OR  
        P(1)        : real part of short echo time image  
        P(2)        : imaginary part of short echo time image  
        P(3)        : real part of long echo time image  
        P(4)        : imaginary part of long echo time image  
         
            Mode = 'PM'  
         
        P(1)        : phase image  
        P(2)        : magnitude image  
              OR  
        P(1)        : phase of short echo time image  
        P(2)        : magnitude of short echo time image  
        P(3)        : real part of long echo time image  
        P(4)        : imaginary part of long echo time image  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_make_fieldmap.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pm_make_fieldmap", *args, **kwargs)
