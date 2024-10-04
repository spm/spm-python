from spm.__wrap__ import _Runtime


def _biopac_acq(*args, **kwargs):
  """  BIOPAC_ACQ is a wrapper to for the reading function from Mathworks file exchange.  
     
    Use as  
      hdr = biopac_acq(filename);  
      dat = biopac_acq(filename, hdr, begsample, endsample, chanindx);  
      evt = biopac_acq(filename, hdr);  
     
    See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
    See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/biopac_acq.m)
  """

  return _Runtime.call("biopac_acq", *args, **kwargs)
