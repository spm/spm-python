from spm._runtime import Runtime


def _opm_fil(*args, **kwargs):
    r"""
      OPM_FIL reads header, data and events from OPM MEG recordings that are done at the FIL (UCL, London).  
         
        Use as  
          hdr = opm_fil(filename);  
          dat = opm_fil(filename, hdr, begsample, endsample, chanindx);  
          evt = opm_fil(filename, hdr);  
         
        See https://github.com/tierneytim/OPM for technical details.  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, QUSPIN_LVM, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/opm_fil.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("opm_fil", *args, **kwargs)
