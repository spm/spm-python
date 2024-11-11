from spm.__wrapper__ import Runtime


def _read_polhemus_fil(*args, **kwargs):
    """
      Reads Polhemus files:  
          either sensor file or headshape file or both  
         
        FORMAT [fid, sens, label] = read_polhemus_fil(Fname_pol,skip)  
        Input:  
        Fname_pol - Polhemus ASCII file containing sensor locations (cm)  
                    (headshape can also be considered here instead of sensors)  
        skip      - first channels to skip  
         
        Output:  
        fid       - fiducial         locations (mm) in rows  
        sens      - sensor/headshape locations (mm) in rows  
        label - labels of the fiducials  
         
        IMPORTANT: Note that Polhemus data files should be -ASCII files with  
        extension .pol  
        It is assumed that the .pol file contains the location (cm) of fiducials  
        (sampled twice), possibly followed by some additional named points and   
        then unnamed location of the sensors.  In some instances the first  
        few channel locations may pertain to reference channels; the skip   
        variable allows these to be skipped if necessary. The fiducial locations  
        are flaged with the strings 'NZ','LE' and 'RE'; indicating the Nasion,  
        left and right eare respectively.  
        _________________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_polhemus_fil.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_polhemus_fil", *args, **kwargs)
