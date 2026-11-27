from spm._runtime import Runtime


def _quspin_lvm(*args, **kwargs):
    r"""
      QUSPIN_LVM reads QuSpin OPM data from the LabVIEW measurement file.  
        See also https://www.ni.com/docs/en-US/bundle/labview/page/labview-measurement-files.html  
         
        Use as  
          hdr = quspin_lvm(filename);  
          dat = quspin_lvm(filename, hdr, begsample, endsample, chanindx);  
          evt = quspin_lvm(filename, hdr);  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, QUSPIN_LVM, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/quspin_lvm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("quspin_lvm", *args, **kwargs)
