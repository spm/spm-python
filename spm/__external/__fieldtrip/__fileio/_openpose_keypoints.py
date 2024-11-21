from spm.__wrapper__ import Runtime


def _openpose_keypoints(*args, **kwargs):
    """
      OPENPOSE_KEYPOINTS reads keypoints from a series of OpenPose JSON files  
         
        Use as  
          hdr = openpose_keypoints(filename);  
          dat = openpose_keypoints(filename, hdr, begsample, endsample, chanindx);  
          evt = openpose_keypoints(filename, hdr);  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/openpose_keypoints.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("openpose_keypoints", *args, **kwargs)
