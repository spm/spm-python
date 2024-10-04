from spm.__wrap__ import _Runtime


def _unicorn_csv(*args, **kwargs):
  """  UNICORN_CSV reads EEG data from the Gtec/Unicorn Hybrid Black  
     
    See http://unicorn-bi.com/  
     
    Use as  
      hdr = unicorn_csv(filename);  
      dat = unicorn_csv(filename, hdr, begsample, endsample, chanindx);  
      evt = unicorn_csv(filename, hdr);  
     
    See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
    See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/unicorn_csv.m)
  """

  return _Runtime.call("unicorn_csv", *args, **kwargs)
