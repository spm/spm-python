from spm.__wrapper__ import Runtime


def _xsens_mvnx(*args, **kwargs):
    """
      XSENS_MVNX reads motion tracking data from a file that was created by XSens MVN  
        motion capture systems. This function is designed to read in .mvnx files from  
        release version 4.  
         
        See https://www.xsens.com/motion-capture  
         
        Use as  
          hdr = xsens_mvnx(filename);  
          dat = xsens_mvnx(filename, hdr, begsample, endsample, chanindx);  
          evt = xsens_mvnx(filename, hdr);  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/xsens_mvnx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("xsens_mvnx", *args, **kwargs)
