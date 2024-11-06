from spm.__wrapper__ import Runtime


def ft_datatype_volume(*args, **kwargs):
    """
      FT_DATATYPE_VOLUME describes the FieldTrip MATLAB structure for volumetric data  
        such as an anatomical MRI.  
         
        The volume data structure represents data on a regular volumetric 3-D grid, like an  
        anatomical MRI, a functional MRI, etc. It can also represent a source reconstructed  
        estimate of the activity measured with MEG. In this case the source reconstruction  
        is estimated or interpolated on the regular 3-D dipole grid (like a box).  
         
        An example volume structure is  
              anatomy: [181x217x181 double]  the numeric data, in this case anatomical information  
                  dim: [181 217 181]         the dimensionality of the 3D volume  
            transform: [4x4 double]          4x4 homogenous transformation matrix, specifying the transformation from voxel coordinates to head or world coordinates  
                 unit: 'mm'                  geometrical units of the coordinate system  
             coordsys: 'ctf'                 description of the coordinate system  
         
        Required fields:  
          - transform, dim  
         
        Optional fields:  
          - anatomy, prob, stat, grey, white, csf, or any other field with dimensions that are consistent with dim  
          - unit, coordsys, fid  
         
        Deprecated fields:  
          - dimord  
         
        Obsoleted fields:  
          - none  
         
        Revision history:  
         
        (2014) The subfields in the avg and trial fields are now present in the  
        main structure, e.g. source.avg.pow is now source.pow. Furthermore, the  
        inside is always represented as logical array.  
         
        (2012b) Ensure that the anatomy-field (if present) does not contain  
        infinite values.  
         
        (2012) A placeholder 2012 version was created that ensured the axes  
        of the coordinate system to be right-handed. This actually never  
        has made it to the default version. An executive decision regarding  
        this has not been made as far as I (JM) am aware, and probably it's  
        a more principled approach to keep the handedness free, so don't mess  
        with it here. However, keep this snippet of code for reference.  
         
        (2011) The dimord field was deprecated and we agreed that volume  
        data should be 3-dimensional and not N-dimensional with arbitrary  
        dimensions. In case time-frequency recolved data has to be represented  
        on a 3-d grid, the source representation should be used.  
         
        (2010) The dimord field was added by some functions, but not by all  
         
        (2003) The initial version was defined  
         
        See also FT_DATATYPE, FT_DATATYPE_DIP, FT_DATATYPE_SOURCE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_datatype_volume.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_datatype_volume", *args, **kwargs)
