from spm.__wrapper__ import Runtime


def _sccn_xdf(*args, **kwargs):
    """
      This is a wrapper to the reading function from the XDF MATLAB toolbox.  
         
        Use as  
          hdr = sccn_xdf(filename);  
          dat = sccn_xdf(filename, hdr, begsample, endsample, chanindx);  
          evt = sccn_xdf(filename, hdr);  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT, XDF2FIELDTRIP  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/sccn_xdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("sccn_xdf", *args, **kwargs)
