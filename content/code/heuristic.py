import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    t1w = create_key('sub-{subject}/anat/sub-{subject}_T1w')
    func=create_key('sub-{subject}/func/sub-{subject}_task-rest_run00{item:01d}_bold')
    info = {t1w: [], func: []}
  

    for idx, s in enumerate(seqinfo):
        if (s.dim1 == 256) and ('MPRAGE_20ch' in s.protocol_name):
            info[t1w].append(s.series_id)
        if (s.dim1 == 64):
            info[func].append(s.series_id)
    return info

