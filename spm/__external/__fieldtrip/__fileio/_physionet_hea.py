from spm._runtime import Runtime


def _physionet_hea(*args, **kwargs):
    r"""
      PHYSIONET_HEA reads data from PhysioNet .hea and .dat files  
         
        Use as  
          hdr = motion_c3d(filename);  
          dat = motion_c3d(filename, hdr, begsample, endsample, chanindx);  
          evt = motion_c3d(filename, hdr);  
         
        This is for data hosted on https://physionet.org following the format   
        documentd on https://wfdb.io  
         
        The format specification is not very clear and example files that I downloaded from  
        Physionet seem to be inconsistent with the specification. The code below works for  
        one example, but your mileage may vary.  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, QUSPIN_LVM, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/physionet_hea.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("physionet_hea", *args, **kwargs)
