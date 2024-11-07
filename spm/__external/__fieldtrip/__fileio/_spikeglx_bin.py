from spm.__wrapper__ import Runtime


def _spikeglx_bin(*args, **kwargs):
    """
      SPIKEGLX_BIN reads Neuropixel data from SpikeGLX .bin files  
         
        See https://github.com/jenniferColonell/SpikeGLX_Datafile_Tools  
         
        Use as  
          hdr = spikeglx_bin(filename);  
          dat = spikeglx_bin(filename, hdr, begsample, endsample, chanindx);  
          evt = spikeglx_bin(filename, hdr);  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/spikeglx_bin.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spikeglx_bin", *args, **kwargs)
