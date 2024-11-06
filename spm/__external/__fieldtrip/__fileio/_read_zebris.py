from spm.__wrapper__ import Runtime


def _read_zebris(*args, **kwargs):
    """
      Reads Zebris files:  
          fiducials locations, and  
          either sensor file or headshape file or both  
         
        FORMAT [fid, sens, label] = read_zebris(Fname_zeb,skip)  
        Input:  
        Fname_zeb  - Zebris ASCII file containing sensor locations (mm)  
                    (headshape can also be considered here instead of sensors)  
        skip       - first channels to skip  
         
        Output:  
        fid        - fiducial         locations (mm) in rows  
        sens       - sensor/headshape locations (mm) in rows  
        label      - labels of the fiducials  
        sens_label - labels of the surface points, electrodes + headshape  
         
        IMPORTANT: Note that Zebris data files should be -ASCII files with  
        extension .sfp  
        It is assumed that the .sfp file contains the location (mm) of fiducials  
        (possibly twice), possibly followed by some additional named points for  
        the electrodes, and then so more named location starting with 'sfl' for  
        headshape locations.  
        In some instances the first few channel locations may pertain to  
        reference channels; the skip variable allows these to be skipped if  
        necessary.  
        The fiducial locations are flaged with the strings 'fidt9','fidnz' and  
        'fidt10'; indicating the leaft ear, nasion, and right ear, respectively.  
        _________________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_zebris.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_zebris", *args, **kwargs)
