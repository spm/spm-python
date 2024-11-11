from spm.__wrapper__ import Runtime


def _qualisys_tsv(*args, **kwargs):
    """
      QUALISYS_TSV reads motion tracking data from a Qualisys tsv file.  
         
        Use as  
          hdr = qualysis_tsv(filename);  
          dat = qualysis_tsv(filename, hdr, begsample, endsample, chanindx);  
          evt = qualysis_tsv(filename, hdr);  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/qualisys_tsv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("qualisys_tsv", *args, **kwargs)
