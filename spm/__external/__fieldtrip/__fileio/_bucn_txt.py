from spm.__wrapper__ import Runtime


def _bucn_txt(*args, **kwargs):
    """
      BUCN_TXT reads the txt files produced by the UCL-Birkbeck NIRS machines, also known  
        as the NTS fNIRS system from Gowerlabs. See https://www.gowerlabs.co.uk/nts  
         
        Use as  
          hdr = bucn_txt(filename);  
          dat = bucn_txt(filename, hdr, begsample, endsample, chanindx);  
          evt = bucn_txt(filename, hdr);  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT, READ_BUCN_NIRSHDR, READ_BUCN_NIRSDATA, READ_BUCN_NIRSEVENT   
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/bucn_txt.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bucn_txt", *args, **kwargs)
