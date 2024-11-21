from spm.__wrapper__ import Runtime


def _coordsys2label(*args, **kwargs):
    """
      COORDSYS2LABEL returns the labels for the three axes, given the symbolic  
        string representation of the coordinate system.  
         
        Use as  
          [labelx, labely, labelz] = coordsys2label(coordsys, format, both)  
         
        The scalar argument 'format' results in return values like these  
          0) 'R'  
          1) 'right'  
          2) 'the right'  
          3) '+X (right)'  
         
        The boolean argument 'both' results in return values like these  
          0) 'right'              i.e. only the direction that it is pointing to  
          1) {'left' 'right'}     i.e. both the directions that it is pointing from and to  
         
        See also FT_DETERMINE_COORDSYS, FT_PLOT_AXES, FT_HEADCOORDINATES, SETVIEWPOINT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/coordsys2label.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("coordsys2label", *args, **kwargs)
