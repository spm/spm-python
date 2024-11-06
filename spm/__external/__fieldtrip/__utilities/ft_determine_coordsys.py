from spm.__wrapper__ import Runtime


def ft_determine_coordsys(*args, **kwargs):
    """
      FT_DETERMINE_COORDSYS plots a geometrical object, allowing you to perform  
        a visual check on the coordinatesystem, the units and on the anatomical  
        labels for the coordinate system axes.  
         
        Use as  
          [dataout] = ft_determine_coordsys(datain, ...)  
        where the input data structure can be either  
         - an anatomical MRI  
         - a cortical or head surface mesh  
         - an electrode, gradiometer or optode definition  
         - a volume conduction model of the head  
        or most other FieldTrip structures that represent geometrical information.  
         
        Additional optional input arguments should be specified as key-value pairs  
        and can include  
          interactive  = string, 'yes' or 'no' (default = 'yes')  
          axisscale    = scaling factor for the reference axes and sphere (default = 1)  
          clim         = lower and upper anatomical MRI limits (default = [0 1])  
         
        This function will pop up a figure that allows you to check whether the  
        alignment of the object relative to the coordinate system axes is correct  
        and what the anatomical labels of the coordinate system axes are. You  
        should switch on the 3D rotation option in the figure panel to rotate and  
        see the figure from all angles. To change the anatomical labels of the  
        coordinate system, you should press the corresponding keyboard button.  
         
        Recognized and supported coordinate systems are 'ctf', 'bti', '4d', 'yokogawa',  
        'eeglab', 'neuromag', 'itab', 'acpc', 'spm', 'mni', 'fsaverage', 'tal', 'scanras',  
        'scanlps', 'dicom'.  
          
        Furthermore, supported coordinate systems that do not specify the origin are 'ras',  
        'als', 'lps', etc. See https://www.fieldtriptoolbox.org/faq/coordsys for more  
        details.  
         
        See also FT_CONVERT_COORDSYS, FT_DETERMINE_UNITS, FT_CONVERT_UNITS, FT_PLOT_AXES, FT_PLOT_XXX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_determine_coordsys.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_determine_coordsys", *args, **kwargs)
