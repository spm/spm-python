from spm.__wrapper__ import Runtime


def _ft_headcoordinates(*args, **kwargs):
    """
      FT_HEADCOORDINATES returns the homogeneous coordinate transformation matrix  
        that converts the specified fiducials in any coordinate system (e.g. MRI)  
        into the rotated and translated headcoordinate system.  
         
        Use as  
          [transform, coordsys] = ft_headcoordinates(fid1, fid2, fid3, coordsys)  
        or  
          [transform, coordsys] = ft_headcoordinates(fid1, fid2, fid3, fid4, coordsys)  
         
        Depending on the desired coordinate system, the order of the fiducials is  
        interpreted as follows  
         
          fid1 = nas  
          fid2 = lpa  
          fid3 = rpa  
          fid4 = extra point (optional)  
         
          fid1 = ac  
          fid2 = pc  
          fid3 = midsagittal  
          fid4 = extra point (optional)  
         
          fid1 = pt1  
          fid2 = pt2  
          fid3 = pt3  
          fid4 = extra point (optional)  
         
          fid1 = bregma  
          fid2 = lambda  
          fid3 = midsagittal  
          fid4 = extra point (optional)  
         
        The fourth argument fid4 is optional and can be specified as an an extra point  
        which is assumed to have a positive Z-coordinate. It will be used to ensure correct  
        orientation of the Z-axis (ctf, 4d, bti, eeglab, yokogawa, neuromag, itab) or  
        X-axis (acpc, spm, mni, tal). The specification of this extra point may result in  
        the handedness of the transformation to be changed, but ensures consistency with  
        the handedness of the input coordinate system.  
         
        The coordsys input argument is a string that determines how the location of the  
        origin and the direction of the axis is to be defined relative to the fiducials:  
          according to CTF conventions:             coordsys = 'ctf'  
          according to 4D conventions:              coordsys = '4d' or 'bti'  
          according to EEGLAB conventions:          coordsys = 'eeglab'  
          according to NEUROMAG conventions:        coordsys = 'itab'  
          according to ITAB conventions:            coordsys = 'neuromag'  
          according to YOKOGAWA conventions:        coordsys = 'yokogawa'  
          according to ASA conventions:             coordsys = 'asa'  
          according to FTG conventions:             coordsys = 'ftg'  
          according to ACPC conventions:            coordsys = 'acpc'  
          according to SPM conventions:             coordsys = 'spm'  
          according to MNI conventions:             coordsys = 'mni'  
          according to Talairach conventions:       coordsys = 'tal'  
          according to PAXINOS conventions:         coordsys = 'paxinos'  
        If the coordsys input argument is not specified, it will default to 'ctf'.  
         
        The CTF, 4D, YOKOGAWA and EEGLAB coordinate systems are defined as follows:  
          the origin is exactly between lpa and rpa  
          the X-axis goes towards nas  
          the Y-axis goes approximately towards lpa, orthogonal to X and in the plane spanned by the fiducials  
          the Z-axis goes approximately towards the vertex, orthogonal to X and Y  
         
        The TALAIRACH, SPM and ACPC coordinate systems are defined as:  
          the origin corresponds with the anterior commissure  
          the Y-axis is along the line from the posterior commissure to the anterior commissure  
          the Z-axis is towards the vertex, in between the hemispheres  
          the X-axis is orthogonal to the midsagittal-plane, positive to the right  
         
        The NEUROMAG and ITAB coordinate systems are defined as follows:  
          the X-axis is from the origin towards the RPA point (exactly through)  
          the Y-axis is from the origin towards the nasion (exactly through)  
          the Z-axis is from the origin upwards orthogonal to the XY-plane  
          the origin is the intersection of the line through LPA and RPA and a line orthogonal to L passing through the nasion  
         
        The ASA coordinate system is defined as follows:  
          the origin is at the orthogonal intersection of the line from rpa-lpa and the line through nas  
          the X-axis goes towards nas  
          the Y-axis goes through rpa and lpa  
          the Z-axis goes approximately towards the vertex, orthogonal to X and Y  
         
        The FTG coordinate system is defined as:  
          the origin corresponds with pt1  
          the x-axis is along the line from pt1 to pt2  
          the z-axis is orthogonal to the plane spanned by pt1, pt2 and pt3  
         
        The PAXINOS coordinate system is defined as:  
          the origin is at bregma  
          the x-axis extends along the Medial-Lateral direction, with positive towards the right  
          the y-axis points from dorsal to ventral, i.e. from inferior to superior  
          the z-axis passes through bregma and lambda and points from cranial to caudal, i.e. from anterior to posterior  
         
        See also FT_ELECTRODEREALIGN, FT_VOLUMEREALIGN, FT_INTERACTIVEREALIGN, FT_AFFINECOORDINATES, COORDSYS2LABEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/ft_headcoordinates.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headcoordinates", *args, **kwargs)
