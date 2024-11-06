from spm.__wrapper__ import Runtime


def ft_datatype_parcellation(*args, **kwargs):
    """
      FT_DATATYPE_PARCELLATION describes the FieldTrip MATLAB structure for parcellated  
        cortex-based data and atlases. A parcellation can either be indexed or probabilistic  
        (see below).  
         
        A parcellation describes the tissue types for each of the surface elements.  
        Parcellations are often, but not always labeled. A parcellatoin can be used to  
        estimate the activity from MEG data in a known region of interest. A surface-based  
        atlas is basically a very detailed parcellation with an anatomical label for each  
        vertex.  
         
        An example of a surface based Brodmann parcellation looks like this  
         
                     pos: [8192x3]         positions of the vertices forming the cortical sheet  
                     tri: [16382x3]        triangles of the cortical sheet  
                coordsys: 'ctf'            the (head) coordinate system in which the vertex positions are expressed  
                    unit: 'mm'             the units in which the coordinate system is expressed  
                brodmann: [8192x1 uint8]   values from 1 to N, the value 0 means unknown  
           brodmannlabel: {Nx1 cell}  
         
        An alternative representation of this parcellation is  
         
                     pos: [8192x3]           positions of the vertices forming the cortical sheet  
                     tri: [16382x3]          triangles of the cortical sheet  
                coordsys: 'ctf'              the (head) coordinate system in which the vertex positions are expressed  
                    unit: 'mm'               the units in which the coordinate system is expressed  
         Brodmann_Area_1: [8192x1 logical]   binary map representing the voxels belonging to the specific area  
         Brodmann_Area_2: [8192x1 logical]   binary map representing the voxels belonging to the specific area  
         Brodmann_Area_3: [8192x1 logical]   binary map representing the voxels belonging to the specific area  
         ...  
         
        The examples above demonstrate that a parcellation can be indexed, i.e. consisting of  
        subsequent integer numbers (1, 2, ...) or probabilistic, consisting of real numbers  
        ranging from 0 to 1 that represent probabilities between 0% and 100%. An extreme case  
        is one where the probability is either 0 or 1, in which case the probability can be  
        represented as a binary or logical array.  
         
        The only difference to the source data structure is that the parcellation structure  
        contains the additional fields xxx and xxxlabel. See FT_DATATYPE_SOURCE for further  
        details.  
         
        Required fields:  
          - pos  
         
        Optional fields:  
          - any field with dimensions that are consistent with pos  
          - unit, coordsys, fid, tri  
         
        Deprecated fields:  
          - none  
         
        Obsoleted fields:  
          - none  
         
        Revision history:  
        (2012/latest) The initial version was defined in accordance with the representation of  
        a voxel-based segmentation.  
         
        See also FT_DATATYPE, FT_DATATYPE_SOURCE, FT_DATATYPE_SEGMENTATION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_datatype_parcellation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_datatype_parcellation", *args, **kwargs)
