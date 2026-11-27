from spm._runtime import Runtime


def _atlas_lookup(*args, **kwargs):
    r"""
      ATLAS_LOOKUP determines the anatomical label of a location in the given atlas.  
         
        Use as  
          label = atlas_lookup(atlas, pos, ...);  
         
        Optional input arguments should come in key-value pairs and can include  
          'method'       = 'sphere' (default) searches surrounding voxels in a sphere  
                           'cube' searches surrounding voxels in a cube  
          'queryrange'   = number, should be 1, 3, 5, 7, 9 or 11 (default = 3)  
          'coordsys'     = 'mni' or 'tal' (default = [])  
         
        Dependent on the coordinates if the input points and the coordinates of the atlas,  
        the input positions are transformed between MNI and Talairach-Tournoux coordinates.  
        See http://www.mrc-cbu.cam.ac.uk/Imaging/Common/mnispace.shtml for more details.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/atlas_lookup.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("atlas_lookup", *args, **kwargs)
